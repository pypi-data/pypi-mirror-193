"""
Optimized configs for selected models. These configs are not necessary, but they can improve performance in some
cases, e.g. training with very small batches or inference with long sequences.

NB: some of these configs get fairly complicated in order to squeeze a bit of extra performance. When developing your
  own config, you can get most of the performance benefits by using auto config -- and maybe splitting MLP layers.
"""
from functools import partial
from itertools import chain
from typing import Callable, Dict, Sequence

import torch
from transformers import BloomConfig, PretrainedConfig, T5Config

from tensor_parallel.communications import CollectiveOperation
from tensor_parallel.slicer_wrapper import Config
from tensor_parallel.tensor_parallel import PerDeviceTensors
from tensor_parallel.utils import nested_map

ConfigGetter = Callable[[PretrainedConfig, Sequence[torch.device]], Config]


def gather_kv(*present_key_value_state, world_size):
    if present_key_value_state[0] is None:
        return present_key_value_state
    else:
        return [tuple(PerDeviceTensors(*item) for item in zip(*present_key_value_state))] * world_size


def select_kv_for_rank(present_key_value_state, rank):
    return nested_map(lambda x: x[rank] if isinstance(x, PerDeviceTensors) else x, present_key_value_state)


def get_bloom_config(model_config: BloomConfig, devices: Sequence[torch.device]) -> Config:
    world_size = len(devices)
    num_heads = model_config.n_head
    head_dim = model_config.hidden_size // num_heads
    gather_kv_across_ranks = CollectiveOperation(
        world_size=world_size, func=lambda *kvs: gather_kv(*kvs, world_size=world_size)
    )  # this operation ensures that we get attention cache for all heads on each device

    _split_alibi = partial(split_alibi, num_heads=num_heads, world_size=world_size)

    return Config(
        state_rules={
            r".*self_attention\.query_key_value\.(weight|bias)$": partial(
                split_heads, dim=0, head_dim=head_dim * 3, world_size=world_size
            ),
            r".*self_attention\.dense\.weight$": partial(split_heads, dim=1, head_dim=head_dim, world_size=world_size),
            r".*self_attention\.dense\.bias$": "scale",
            r".*mlp\.dense_h_to_4h\.(weight|bias)$": "split 0",
            r".*mlp\.dense_4h_to_h\.weight$": "split 1",
            r".*mlp\.dense_4h_to_h\.bias$": "scale",
            r".*word_embeddings.weight$": "split 1",
            # note: ^-- lm_head.weight is tied with word_embeddings
        },
        input_rules={
            r".*self_attention$": {"layer_past": select_kv_for_rank, "alibi": _split_alibi},
            r".*lm_head$": {0: "split -1"},  # note: we need to split lm_head inputs because
            # ... lm_head's weights (tied embeddings) are already split across input dimension
        },
        output_rules={
            r".*self_attention$": {1: gather_kv_across_ranks},
            r".*self_attention\.dense$": {0: "sum"},
            r".*mlp\.dense_4h_to_h$": {0: "sum"},
            r".*word_embeddings$": {0: "gather -1"},
            r".*lm_head$": {0: "sum"},
        },
        attr_rules={r".*self_attention$": {"num_heads": partial(split_num_heads, world_size=world_size)}},
    )


def split_heads(tensor: torch.Tensor, *, dim: int, head_dim: int, rank: int, world_size: int, optional: bool = False):
    """Split a tensor along dim such that each part size is divisible by head_dim"""
    if tensor is None and optional:
        return None
    assert tensor.shape[dim] % head_dim == 0, tensor.shape
    if dim < 0:
        dim = (tensor.ndim + dim) % tensor.ndim
    shape = list(tensor.shape)
    shape[dim] //= head_dim
    shape.insert(dim + 1, head_dim)
    tensor_part = tensor.reshape(shape).tensor_split(world_size, dim=dim)[rank].flatten(dim, dim + 1)
    return tensor_part


def split_num_heads(num_heads: int, *, rank: int, world_size: int):
    return torch.empty(num_heads, device="meta").tensor_split(world_size)[rank].numel()


def split_inner_dim(inner_dim: int, *, rank: int, num_heads: int, world_size: int):
    return split_num_heads(num_heads=num_heads, rank=rank, world_size=world_size) * (inner_dim // num_heads)


def split_alibi(alibi: torch.Tensor, *, rank: int, num_heads: int, world_size: int) -> torch.Tensor:
    """split alibi tensor of shape [batch_size * num_heads, ...] over attention heads"""
    alibi_expanded = alibi.reshape(-1, num_heads, *alibi.shape[1:])
    alibi_part = alibi_expanded.tensor_split(world_size, dim=1)[rank]
    return alibi_part.reshape(-1, *alibi.shape[1:])


def get_t5_config(model_config: T5Config, devices: Sequence[torch.device]) -> Config:
    world_size = len(devices)
    num_heads = model_config.num_heads
    head_dim = model_config.d_kv

    gather_kv_across_ranks = CollectiveOperation(
        world_size=world_size, func=lambda *kvs: gather_kv(*kvs, world_size=world_size)
    )  # this operation ensures that we get attention cache for all heads on each device

    def select_kv_for_rank(*kvs, rank):
        if kvs[0] is None:
            return None
        else:
            kvs = kvs[0]
            return (kvs[0][rank], kvs[1][rank])

    return Config(
        state_rules={
            r".*SelfAttention\.q\.(weight|bias)$": partial(
                split_heads, dim=0, head_dim=head_dim, world_size=world_size
            ),
            r".*SelfAttention\.k\.(weight|bias)$": partial(
                split_heads, dim=0, head_dim=head_dim, world_size=world_size
            ),
            r".*SelfAttention\.v\.(weight|bias)$": partial(
                split_heads, dim=0, head_dim=head_dim, world_size=world_size
            ),
            r".*relative_attention_bias\.weight$": "split 1",
            r".*SelfAttention\.o\.weight$": partial(split_heads, dim=1, head_dim=head_dim, world_size=world_size),
            r".*DenseReluDense\.wi\.weight$": "split 0",
            r".*DenseReluDense\.wi_0\.weight$": "split 0",
            r".*DenseReluDense\.wi_1\.weight$": "split 0",
            r".*DenseReluDense\.wo\.weight$": "split 1",
            r".*shared.weight$": "split 1",
            r".*lm_head\.weight$": "split 1",
            # note: ^-- lm_head.weight tied with word embeddings
        },
        input_rules={
            r".*SelfAttention$": {"past_key_value": select_kv_for_rank},
            r".*lm_head$": {0: "split -1"},  # note: we need to split lm_head inputs because
            # ... lm_head's weights (tied embeddings) are already split across input dimension
        },
        output_rules={
            r".*SelfAttention$": {0: "sum", 1: gather_kv_across_ranks},
            r".*DenseReluDense$": {0: "sum"},
            r".*shared$": {0: "gather -1"},
            r".*lm_head$": {0: "sum"},
        },
        attr_rules={
            r".*SelfAttention$": {
                "n_heads": partial(split_num_heads, world_size=world_size),
                "inner_dim": partial(split_inner_dim, num_heads=model_config.num_heads, world_size=world_size),
            },
            r".*relative_attention_bias$": {"embedding_dim": partial(split_num_heads, world_size=world_size)},
        },
    )


PREDEFINED_CONFIGS: Dict[str, ConfigGetter] = {
    "BloomModel": get_bloom_config,
    "T5ForConditionalGeneration": get_t5_config,
}

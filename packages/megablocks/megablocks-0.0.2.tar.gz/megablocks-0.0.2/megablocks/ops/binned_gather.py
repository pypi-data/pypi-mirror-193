# NOTE: Torch needs to be imported before the custom
# extensions. Otherwise libc10.so cannot be found.
import torch

from stk.backend.autocast import custom_fwd, custom_bwd

# TODO(tgale): Wrap this in a try-block with better
# error message and instructions for building the
# c++ operations.
import megablocks_ops as ops

# Autograd wrapper for binned_gather kernel.
class BinnedGatherOp(torch.autograd.Function):

    @staticmethod
    @custom_fwd
    def forward(ctx, x, indices, bins, bin_size):
        ctx.save_for_backward(indices, bins)
        return ops.binned_gather(x, indices, bins, bin_size)

    @staticmethod
    @custom_bwd
    def backward(ctx, grad):
        indices, bins = ctx.saved_tensors
        return ops.binned_scatter(grad, indices, bins), None, None, None
binned_gather = BinnedGatherOp.apply

import torch
import torch.nn as nn


class DefaultLoss(nn.Module):
    def __init__(self):
        super(DefaultLoss, self).__init__()

    def forward(self, *args, **kwargs):
        return torch.tensor(0.0)  # Placeholder for a default loss value


def get_loss_fn(name):
    return DefaultLoss()
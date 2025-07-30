import torch
import torch.nn as nn


class DefaultModel(nn.Module):
    def __init__(self):
        super(DefaultModel, self).__init__()
        self.pass_through = nn.Identity()

    def forward(self, x):
        return self.pass_through(x)

def build_model(name):
    return DefaultModel()

# default loader is a class with ayield function that returns an empty tensor
import torch


class DefaultLoader:
    def __init__(self, cfg):
        self.cfg = cfg

    def __iter__(self):
        yield torch.tensor([])

def get_data_loader(cfg, split="train"):
    return DefaultLoader(cfg)
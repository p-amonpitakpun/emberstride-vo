from domain.model.builder import build_model
from domain.losses import get_loss_fn
from infrastructure.data.tum_loader import get_data_loader
from infrastructure.logger.wandb_logger import WandBLogger

import torch


class Trainer:
    def __init__(self, cfg):
        self.cfg = cfg
        self.device = torch.device(cfg.device if torch.cuda.is_available() else "cpu")

        self.model = build_model(cfg.model).to(self.device)
        self.criterion = get_loss_fn(cfg.loss).to(self.device)
        # self.optimizer = torch.optim.Adam(
        #     self.model.parameters(), lr=cfg.lr
        # )

        self.train_loader = get_data_loader(cfg.data, split="train")
        self.val_loader = get_data_loader(cfg.data, split="val")

        self.logger = WandBLogger(cfg)

    def train_epoch(self):
        return
    
    def validate(self):
        return
    
    def run(self):
        return
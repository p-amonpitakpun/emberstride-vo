import yaml
from utils.dotdict import DotDict
from application.trainer import Trainer

def load_config(path: str):
    with open(path, "r") as f:
        return yaml.safe_load(f)

if __name__ == "__main__":
    cfg = DotDict(load_config("config/cloud.yaml"))
    trainer = Trainer(cfg)
    trainer.run()

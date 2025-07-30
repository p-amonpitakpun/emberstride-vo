import yaml
from utils.dotdict import DotDict
from application.trainer import Trainer

def load_config(path: str):
    with open(path, "r") as f:
        return yaml.safe_load(f)

if __name__ == "__main__":
    print("This is a placeholder for the main module.")
    cfg = DotDict(load_config("config/default.yaml"))
    trainer = Trainer(cfg)
    trainer.run()
import argparse
import yaml


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt",type=str,help="path of checkpoint")
    parser.add_argument("--gpus",type=list,default=[],help="like [0,1,2]. [] means cpu")
    parser.add_argument("--epochs", type=int, default=200,help="train epochs")
    parser.add_argument("--config", type=str, help="config yaml/yml file path")
    args= parser.parse_args()
    if args.config:
        with open(args.config) as f:
            content = yaml.safe_load(f)
        parser.set_defaults(**content)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    print(parse_args())

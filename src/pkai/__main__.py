import argparse
from os.path import dirname, abspath

import torch

from pkai.protein import Protein


def load_model(model_name: str, device):
    path = dirname(abspath(__file__))
    fname = f"{model_name}_model.pt"
    fpath = f"{path}/models/{fname}"

    device = torch.device(device)
    model = torch.jit.load(f"{fpath}").to(device)

    return model


def pkai(pdb, model_name="pkai", device="cpu", threads=None):
    if threads:
        torch.set_num_threads(threads)
    model = load_model(model_name, device)
    prot = Protein(pdb)
    prot.apply_cutoff()
    pks = prot.predict_pkas(model, device)
    return pks


def main():
    parser = argparse.ArgumentParser(description="pkai")
    parser.add_argument("pdb_file", type=str, help="PDB file")
    parser.add_argument(
        "--model",
        type=str,
        choices=["pkai", "pkai+"],
        help="Number of threads to use",
        default="pkai",
    )
    parser.add_argument(
        "--device", type=str, help="Device on which to run the model on", default="cpu"
    )
    parser.add_argument("--threads", type=str, help="Number of threads to use")

    args = parser.parse_args()

    pkai(args.pdb_file, model_name=args.model, device=args.device, threads=args.threads)


if __name__ == "__main__":
    main()

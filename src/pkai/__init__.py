from os.path import dirname, abspath

import torch

from pkai.protein import Protein

name = "pkai"


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

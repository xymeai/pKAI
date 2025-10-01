import argparse

from pkai import pkai


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

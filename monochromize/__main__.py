from argparse import ArgumentParser, Namespace

from monochromize import monochromize


def main() -> None:
    parser = ArgumentParser(description="Tool to report testing results.")
    parser.add_argument(
        "image",
        type=str,
        metavar="IMAGE",
        help="path to image file.",
        default=None,
    )
    args: Namespace = parser.parse_args()
    monochromize(args.image)


if __name__ == "__main__":
    main()

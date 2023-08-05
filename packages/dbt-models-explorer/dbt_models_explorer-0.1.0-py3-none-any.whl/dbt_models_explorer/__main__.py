import sys
from argparse import ArgumentParser

from .loader import RUNTIME_ERRORS, load_from_yaml
from .render import print_relationships, write_csv

ap = ArgumentParser(
    prog="", description=""
)
ap.add_argument(
    "path",
    type=str,
    help="Path of the directory where the files are",
)
ap.add_argument(
    "--format",
    type=str,
    const="rich",
    nargs="?",
    choices=["rich", "csv"],
    help="Format for output, (default: %(const)s)",
    default="rich",
)
ap.add_argument(
    "--filename",
    type=str,
    default="relationships.csv",
    nargs="?",
    help="Name for the file when the --format option generates a file, (default: %(default)s)",
)


def main():
    args = ap.parse_args()
    if not args.path:
        ap.print_help()
        return 1
    tables = load_from_yaml(args.path)
    if args.format == 'rich':
        print_relationships(tables)
    elif args.format == 'csv':
        write_csv(tables, args.filename)


if __name__ == "__main__":
    sys.exit(main())

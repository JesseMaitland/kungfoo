import sys
import inspect
from pathlib import Path
from typing import Dict
from argparse import ArgumentParser, Namespace

sys.path.append(Path.cwd().as_posix())
from kungfoo import moves


def get_moves() -> Dict:
    return dict(inspect.getmembers(moves, inspect.isfunction))


def parse_args() -> Namespace:
    move_names = get_moves().keys()

    parser = ArgumentParser()
    parser.add_argument("move", choices=move_names)

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    move = get_moves()[args.move]
    move()


main()

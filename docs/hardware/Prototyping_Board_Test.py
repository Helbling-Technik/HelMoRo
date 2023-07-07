#!/usr/bin/python3

import argparse
import shape

DEFAULT_HEIGHT = 46.0
DEFAULT_WIDTH = 61.0

parser = argparse.ArgumentParser()
parser.add_argument("--height", help=f"Shape height in mm's (default={DEFAULT_HEIGHT})", type=float, default=DEFAULT_HEIGHT)
parser.add_argument("--width", help=f"Shape width in mm's (default={DEFAULT_WIDTH})", type=float, default=DEFAULT_WIDTH)

args = parser.parse_args()

s = shape.Shape({"height": args.height, "width": args.width})

print(s.render())
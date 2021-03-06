#!/bin/env python3

import argparse, os

import fileformats, romfs, exefs, slb2

modes = {
    "guess": fileformats.guess,
    "romfs": romfs.process,
    "exefs": exefs.process,
    "slb2": slb2.process
}

parser = argparse.ArgumentParser(description="pack/unpack tool for various 3ds file formats")
parser.add_argument("--input", "-i", type=str)
parser.add_argument("--output", "-o", type=str, default="dump")
parser.add_argument("--mode", "-m", type=str, default="guess")
parser.add_argument("--unpack", "-u", help="unpacks file", action="store_true")
parser.add_argument("--pack", "-p", help="packs directory", action="store_true")

args = parser.parse_args()

if args.pack == args.unpack:
    parser.print_help()
    exit(1)

if not args.mode in modes.keys():
    print("Available modes:")
    for key, val in modes.items():
        print(f"\t{key}")
    exit(1)

modes[args.mode](args.input, args.output, args.pack)

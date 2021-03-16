import os
from tools import *

def process(in_file, out_file, should_pack):
    if not should_pack:
        if not os.path.isfile(in_file) or not os.path.isdir(out_file):
            print("Invalid input or output!")
            return

        with open(in_file, "rb") as buf:
            sig = rd_str(buf, 0x100)
            magic = rd_str(buf, 4)

            print(f"magic: {magic}")

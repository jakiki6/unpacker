import os

from tools import *

def process(in_file, out_file, should_pack):
    if not should_pack:
        if not os.path.isfile(in_file) or not os.path.isdir(out_file):
            print("Invalid input or output!")
            return
        with open(in_file, "rb") as buf:
            magic = rd_str(buf, 8)
            type = rd_le(buf, 8)
            hmac_key_id = rd_le(buf, 8)
            num_sections = rd_le(buf, 8)
            header_size = rd_le(buf, 8)
            total_sections_size = rd_le(buf, 8)

            print(f"magic: {magic}\ntype: {type}\nhmac key id: {hmac_key_id}\nnumber of sections: {num_sections}\nheader size: {header_size}\ntotal sections size: {total_sections_size}")

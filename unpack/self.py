# https://www.psdevwiki.com/ps4/SELF_File_Format

import os
from tools import *

def process(in_file, out_file, should_pack):
    if not should_pack:
        if not os.path.isfile(in_file) or not os.path.isdir(out_file):
            print("Invalid input or output!")
            return

        with open(in_file, "rb") as buf:
            magic = rd_str(buf, 4)
            unknown1 = rd_str(buf, 4)
            content_type = rd_le(buf, 1)
            program_type = rd_le(buf, 1)
            padding1 = rd_le(buf, 2)
            header_size = rd_le(buf, 2)
            sig_size = rd_le(buf, 2)
            self_size = rd_le(buf, 4)
            padding2 = rd_str(buf, 4)
            num_sections = rd_le(buf, 2)
            unknown2 = rd_str(buf, 2)
            padding3 = rd_le(buf, 4)

            print(
                f"magic: {magic}\nunknown: {unknown1}\ncontent type: {content_type}\nprogram type: {program_type}\npadding: {padding1}\nheader size: {header_size}\nsignature size: {sig_size}\n" + \
                f"self size: {self_size}\npadding: {padding2}\nnumber of sections: {num_sections}\nunknown: {unknown2}\npadding: {padding3}\nsections:"
            )

            segments = []
            for i in range(0, num_sections):
                flags = rd_le(buf, 8)
                offset = rd_le(buf, 8)
                packed_size = rd_le(buf, 8)
                unpacked_size = rd_le(buf, 8)

                print(f"\t{i}:")
                print(f"\t\toffset: {offset}\n\t\tpacked size: {packed_size}\n\t\tunpacked size: {unpacked_size}")
                print(f"\t\tflags: ", end="")
                if flags & 0x1:
                    print("ordered", end=" ")
                if flags & 0x2:
                    print("encrypted", end=" ")
                if flags & 0x4:
                    print("signed", end=" ")
                if flags & 0x8:
                    print("deflated", end=" ")
                if flags & 0x800:
                    print("block", end=" ")
                print()

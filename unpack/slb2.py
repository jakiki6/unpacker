import os
from tools import *

def process(in_file, out_file, should_pack):
    if not os.path.isfile(in_file) or not os.path.isdir(out_file):
        print("Invalid input or output!")
        return

    with open(in_file, "rb") as buf:
        magic = rd_str(buf, 4)
        version = rd_le(buf, 4)
        flags = rd_le(buf, 4)
        num = rd_le(buf, 4)
        size_in_sectors = rd_le(buf, 4) # sector size is 512 bytes
        padding = rd_str(buf, 3 * 4)

        print(f"magic: {magic}\nversion: {version}\nflags: 0x{hex(flags)[2:].zfill(2)}\nnumber of files: {num}\nsize in sectors: {size_in_sectors}\n12 bytes padding: {padding}")

        print("files:")

        for i in range(0, num):
            start = rd_le(buf, 4) * 512 # times 512 because the value is in sectors
            size = rd_le(buf, 4)
            padding = rd_str(buf, 2 * 4)
            fname = rd_str(buf, 32).rstrip(b"\x00").decode()
            print(f"\t{fname}:\n\t\tstart: {start}\n\t\tsize: {size}\n\t\tpadding: {padding}")

            orig_offset = buf.tell()

            buf.seek(start)
            with open(os.path.join(out_file, fname), "wb") as outf:
                for i in range(0, (size + 512) // 512):
                    outf.write(buf.read(512))
            buf.seek(orig_offset)

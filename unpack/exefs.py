import os
from tools import *

def process(in_file, out_file, should_pack):
    if not should_pack:
        if not os.path.isfile(in_file) or not os.path.isdir(out_file):
            print("Invalid input or output!")
            return

        with open(in_file, "rb") as buf:
            files = []
            print("files:")
            for i in range(0, 10):
                name = rd_str(buf, 8).decode().rstrip("\x00")
                offset = rd_le(buf, 4) + 0x200
                size = rd_le(buf, 4)
                if name != "":
                    print(f"\t{name} at {offset} with size {size}")
                    files.append({
                        "name": name,
                        "offset": offset,
                        "size": size
                    })
            for file in files:
                buf.seek(file["offset"])
                print(f"writing {file['name']}")
                with open(os.path.join(out_file, file["name"]), "wb") as f:
                    for i in range(0, file["size"], 512):
                        f.write(buf.read(512))

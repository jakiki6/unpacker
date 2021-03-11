import os
from tools import *

def process(in_file, out_file, should_pack):
    if not should_pack:
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

            print(f"magic: {magic}\nversion: {version}\nflags: 0x{hex(flags)[2:].zfill(8)}\nnumber of files: {num}\nsize in sectors: {size_in_sectors}\n12 bytes padding: {padding}")

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
                    for i in range(0, size // 512):
                        outf.write(buf.read(512))
                    outf.write(buf.read(size % 512))
                buf.seek(orig_offset)

    else:
        if not os.path.isdir(in_file):
            print("Invalid input or output!")
            return

        root, _, filenames = next(os.walk(in_file))
        filenames = sorted(filenames, key = lambda s: sum(map(ord, s)))

        files = []

        for filen in filenames:
            with open(os.path.join(root, filen)) as file:
                if len(filen) > 32:
                    print(f"name {filen} is too long!")
                    continue
                file.seek(0, 2)
                files.append({
                    "size": file.tell(),
                    "name": filen,
                    "path": os.path.join(root, filen)
                })
        with open(out_file, "wb") as buf:
            wr_str(b"SLB2", buf)    # magic
            wr_le(2, buf, 4)        # version
            wr_le(0, buf, 4)        # flags
            wr_le(len(files), buf, 4)
            seek_len = buf.tell()   # save for later
            wr_le(0, buf, 4)        # dummy value
            wr_str(b"\x00" * 4 * 3, buf)

            offset = align(buf.tell(), 512) + 512
            for file_data in files:
                file_data["offset"] = offset
                wr_le(offset // 512, buf, 4)
                wr_le(file_data["size"], buf, 4)
                wr_str(b"\x00" * 4 * 2, buf)
                wr_str(file_data["name"].encode() + b"\x00" * (32 - len(file_data["name"])), buf)
                offset = align(offset + file_data["size"], 512)

            for file_data in files:
                print(f"writing {file_data['name']}")
                buf.seek(file_data["offset"])
                with open(file_data["path"], "rb") as infile:
                    for i in range(0, align(file_data["size"], 512) // 512):
                        buf.write(infile.read(512))
                    buf.write(infile.read(file_data["size"] % 512))

            length = align(buf.tell(), 512)
            buf.seek(seek_len)
            wr_le(length // 512, buf, 4)

            buf.seek(0, 2)
            print(f"padding {buf.tell() % 512} bytes")
            while buf.tell() % 512:
                buf.write(bytes([0]))

            print("You need to patch the SLB2 file if you're using a newer firmware version")

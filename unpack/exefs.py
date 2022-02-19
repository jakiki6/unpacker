import os
from tools import *

class ExeFSReader(object):
    def __init__(self, buf, handler):
        self.buf = buf
        self.handler = handler

    def parse(self):
        files = []
        for i in range(0, 10):
            name = rd_str(self.buf, 8).decode().rstrip("\x00")
            offset = rd_le(self.buf, 4) + 0x200
            size = rd_le(self.buf, 4)
            if name != "":
                files.append({   
                    "name": name,
                    "offset": offset,
                    "size": size
                })

        for file in files:
            view = self.buf.view(file["offset"])
            handle = self.handler.handle(file["name"])
            size = file["size"]
            while size > 0:
                handle.write(view.read(512))
                size -= 512

def process(in_file, out_file, should_pack):
    if not should_pack:
        if not os.path.isfile(in_file) or not os.path.isdir(out_file):
            print("Invalid input or output!")
            return

        with open(in_file, "rb") as buf:
            reader = ExeFSReader(BufWrapper(buf), FsHandler(out_file))
            reader.parse()

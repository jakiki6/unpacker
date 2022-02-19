import os

class BufWrapper(object):
    def __init__(self, buf, pos=0):
        self.buf = buf
        self.pos = pos

    def read(self, amount):
        self.buf.seek(self.pos, 0)
        self.pos += amount
        return self.buf.read(amount)

    def write(self, data):
        self.buf.seek(self.pos, 0)
        self.pos += len(data)
        self.buf.write(data)

    def seek(self, address):
        self.pos = address

    def seek_rel(self, offset):
        self.pos += offset

    def view(self, address):
        return BufWrapper(self.buf, address)

class FsHandler(object):
    def __init__(self, root):
        self.root = root

    def handle(self, key):
        key = os.path.join(self.root, key)
        d = "/".join(key.split("/")[:-1])

        if not os.path.exists(d):
            os.makedirs(d)

        return open(key, "wb")

def rd_str(buf, num):
    return buf.read(num)

def rd_le(buf, num):
    return int.from_bytes(buf.read(num), "little")

def wr_str(string, buf):
    buf.write(string)

def wr_le(val, buf, num):
    try:
        buf.write(val.to_bytes(length=num, byteorder="little"))
    except:
        raise OverflowError(f"{val} doesn't fit in {num} byte(s)")

def align(num, al):
    while num % al:
        num += 1
    return num

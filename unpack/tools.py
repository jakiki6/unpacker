def rd_str(buf, num):
    return buf.read(num)

def rd_le(buf, num):
    return int.from_bytes(buf.read(num), "little")

def align(num, al):
    return num + (al - (num % al))

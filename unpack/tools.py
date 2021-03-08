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
    if num % al:
        num += al - (num % al)
    return num

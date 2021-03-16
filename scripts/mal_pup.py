def wr_str(string, buf):
    buf.write(string)

def wr_le(val, buf, num):
    try:
        buf.write(val.to_bytes(length=num, byteorder="little"))
    except:
        raise OverflowError(f"{val} doesn't fit in {num} byte(s)")

with open("PS4UPDATE.PUP", "wb") as buf:
    wr_str(b"SLB2", buf)

    wr_le(2, buf, 4)
    wr_le(0, buf, 4)

    wr_le(100, buf, 4)
    wr_le(1, buf, 4)

    wr_str(b"\x00" * (512 - buf.tell()), buf)

# extracts all .c and .h file mentioned in a kernel dump of the ps4
# tags: ps4 kernel dump strings source-code

i = 0
d = b"W:\\Build\\J02387083"
offsets = []
strings = []

with open("dump.elf", "rb") as buf:
    a = b""
    while True:
        a = buf.read(1)
        if not a:
            break
        if a[0] == d[i]:
            i += 1
            if i == len(d):
                offsets.append(buf.tell() - i)
                i = 0
        else:
            i = 0
    for offset in offsets:
        buf.seek(offset)
        string = b""
        while True:
            string += buf.read(1)
            if (string[-1] == b"c"[0] or string[-1] == b"h"[0]) and string[-2] == b"."[0]:
                break
        strings.append(string)

with open("strings.txt", "w") as file:
    for string in strings:
        try:
            file.write(string.decode() + "\n")
        except:
            pass

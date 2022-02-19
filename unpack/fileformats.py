import exefs, romfs, slb2, scecaf, self

magics = {
    b".code": exefs.process,    # .code is commonly the first file in exefs
    b"IVFC": romfs.process,
    b"SLB2": slb2.process,
    b"SCECAF\x00\x00": scecaf.process,
    b"\x4f\x15\x3d\x1d": self.process
}

def guess(in_file, out_file, should_pack):
    hit = False
    if True:
#    try:
        with open(in_file, "rb") as file:
            for key, val in magics.items():
                file.seek(0)
                if key == file.read(len(key)):
                    print(f"Found file format for magic {key}")
                    hit = True
                    val(in_file, out_file, should_pack)
                    break
#    except FileNotFoundError:
#        print(f"{in_file} not found")
    if not hit:
        print("Magic not found")

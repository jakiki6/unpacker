def decode(string):
    res = b""
    for i in range(0, len(string), 2):
        res += bytes.fromhex(string[i:i+2])
    return res

FW_AES = decode("5301c28824b57137a819c042fc119e3f")
FW_CMAC = decode("8f215691ac7ef6510239dd32cc6a2394")

PTCH_AES = decode("ef90b21b31452379068e3041aad8281e")
PTCH_CMAC = decode("95b1aaf20c16d46fc816df32551de032")

RL78_Id = decode("3a4e6f743a557365643a")

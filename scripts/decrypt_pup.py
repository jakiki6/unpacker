import keys
from Crypto.Cipher import AES    
import sys

cipher = AES.new(keys.PTCH_AES, AES.MODE_CBC)

try:
    with open(sys.argv[1], "rb") as ifile:
        with open(sys.argv[2], "wb") as ofile:
            ofile.write(cipher.decrypt(ifile.read()))

except FileNotFoundError:
    print("Specify an input and output file!")

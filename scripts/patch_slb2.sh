#!/bin/bash

# Patches produced SLB2 with extracted unknown part from 0x200

dd if=samples/enc.bin of=PS4UPDATE.PUP bs=512 seek=1 conv=notrunc

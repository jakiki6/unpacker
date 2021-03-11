#!/bin/bash

mount /dev/sdc1 /mnt
cp PS4UPDATE.PUP /mnt/PS4/UPDATE/
sync
umount /mnt

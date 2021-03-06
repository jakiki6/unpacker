from tools import *

def process(in_file, out_file, should_pack):
    with open(in_file, "rb") as buf:
        if not should_pack:
            magic_str = rd_str(buf, 4)
            magic_num = rd_le(buf, 4)
            master_hash_size = rd_le(buf, 4)
            l1_logical_offset = rd_le(buf, 8) + 0x1000
            l1_hashdata_size = rd_le(buf, 8)
            l1_block_size = 2 ** rd_le(buf, 4)
            l1_reserved = rd_str(buf, 4)
            l2_logical_offset = rd_le(buf, 8)
            l2_hashdata_size = rd_le(buf, 8) + 0x1000
            l2_block_size = 2 ** rd_le(buf, 4)
            l2_reserved = rd_str(buf, 4)
            l3_logical_offset = rd_le(buf, 8) + 0x1000
            l3_hashdata_size = rd_le(buf, 8)
            l3_block_size = 2 ** rd_le(buf, 4)
            l3_reserved = rd_str(buf, 4)
            reserved_1 = rd_str(buf, 4)
            reserved_2 = rd_str(buf, 4)
            opt_info_size = rd_str(buf, 4)

            print(f"magic:\n\tstring: {magic_str}\n\tnum: {hex(magic_num)}")
            print(f"master hash size: {master_hash_size}")
            print(f"level 1 partition:\n\toffset: {l1_logical_offset}\n\thashdata size: {l1_hashdata_size}\n\tblock size: {l1_block_size}")
            print(f"level 2 partition:\n\toffset: {l2_logical_offset}\n\thashdata size: {l2_hashdata_size}\n\tblock size: {l2_block_size}")
            print(f"level 3 partition:\n\toffset: {l3_logical_offset}\n\thashdata size: {l3_hashdata_size}\n\tblock size: {l3_block_size}")

            buf.seek(align(l3_logical_offset, l3_block_size))
            l3_header_length = rd_le(buf, 4)
            dir_ht_offset = rd_le(buf, 4) + l3_logical_offset
            dir_ht_length = rd_le(buf, 4)
            dir_md_offset = rd_le(buf, 4) + l3_logical_offset
            dir_md_length = rd_le(buf, 4)
            file_ht_offset = rd_le(buf, 4) + l3_logical_offset
            file_ht_length = rd_le(buf, 4)
            file_md_offset = rd_le(buf, 4) + l3_logical_offset
            file_md_length = rd_le(buf, 4)
            file_data_offset = rd_le(buf, 4) + l3_logical_offset

            print(f"level 3 header has {l3_header_length} bytes")

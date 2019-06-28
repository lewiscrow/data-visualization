import struct
import string

datafile = 'ch02-fixed-width-1M.data'

#定义掩码规则（长度为9的字符串+长度为15的字符串+长度为5的字符串）
mask='9s14s5s'

with open(datafile, 'r') as f:
    for line in f:
        fields = struct.Strct(mask).unpack_from(bytes(line.encode("utf-8")))
        for field in fields:
            print(field.strip())
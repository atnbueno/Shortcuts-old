# color2plte.py by @atnbueno (/u/atnbueno), inspired by @pfg (/u/pfg___)
# Version 0.2 (2018-12-23) License: MIT

# This program generates a base64-encoded 8-color monochrome PNG palette from an #RRGGBB color

# WARNING: No error checking

import binascii
from struct import pack
from sys import argv

# Converts color to binary data
if len(argv) == 2:
    color = argv[1]
if color[0] == '#':
    color = color[1:7]
color = binascii.unhexlify(color)

# Assembles PLTE binary data
binary_plte = b'PLTE\x00\x00\x00' + 7 * color
binary_plte = pack('!I', 24) + binary_plte + pack('!I', binascii.crc32(binary_plte))

# Base64 output
print(binascii.b2a_base64(binary_plte, newline=False).decode('ascii'))

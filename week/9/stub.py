#!/usr/bin/env python2

import sys
import struct



# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

SECTION_ASCII = 1
SECTION_UTF8 = 2
SECTION_WORDS = 3
SECTION_DWORDS = 4
SECTION_DOUBLES = 5
SECTION_COORD = 6
SECTION_REFERENCE = 7
SECTION_PNG = 8
SECTION_GIF87 = 9
SECTION_GIF89 = 10


if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])
timestamp, author = struct.unpack("<L8s", data[8:20])
(section,) = struct.unpack("<L", data[20:24])


if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))


print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %d" % int(timestamp))
print("AUTHOR: %s" % str(author))
print("SECTIONS: %d" % int(section))


# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")

offset = 24
i = 0

while i < int(section):

    stype, slen = struct.unpack("<LL", data[offset:offset+8])
    slen = int(slen)

    if stype == SECTION_ASCII:
        (output,) = struct.unpack(("<%ds" % slen), data[offset + 8: (offset + 8 + slen)])
        print("ASCII OUTPUT: %s" % (output))
        
    elif stype == SECTION_UTF8:
        
        print()
    elif stype == SECTION_WORDS:
        print()
    elif stype == SECTION_DWORDS:
        print()
    elif stype == SECTION_DOUBLES:
        print()
    elif stype == SECTION_COORD:
        print()
    elif stype == SECTION_REFERENCE:
        print()
    elif stype == SECTION_PNG:
        print()
    elif stype == SECTION_GIF87:
        print()
    elif stype == SECTION_GIF89:
        print()
        
    offset = offset + slen + 8
    i = i + 1

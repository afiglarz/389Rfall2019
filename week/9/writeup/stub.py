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

def proc_image_gif(name, ext, data):
    fname = name + "." + ext
    image = open(fname, "wb")
    image.write(data)
    print ("Image/gif generated with name %s" % fname)

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

if section <= 0:
    bork("RECIEVED NEGATIVE NUMBER OF SECTIONS")

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
        (output,) = struct.unpack(("<%ds" % slen), data[offset + 8: (offset + 8 + slen)])
        output = output.decode('utf-8')
        print("UTF-8 OUTPUT: %s" % (output))
        
    elif stype == SECTION_WORDS:
        words = int(slen/4)
        frmt_str = "<" + ("%s" % 'L' * words)
        (output,) = struct.unpack(frmt_str, data[offset + 8: (offset + 8 + slen)])
        print("WORDS OUTPUT: %s" % (output))
        
    elif stype == SECTION_DWORDS:
        dwords = int(slen/8)
        frmt_str = "<" + ("%s" % 'L' * dwords)
        (output,) = struct.unpack(frmt_str, data[offset + 8: (offset + 8 + slen)])
        print("DWORDS OUTPUT: %s" % (output))

    elif stype == SECTION_DOUBLES:
        doubles = int(slen/8)
        frmt_str = "<" + ("%s" % 'L' * doubles)
        (output,) = struct.unpack(frmt_str, data[offset + 8: (offset + 8 + slen)])
        print("DOUBLES OUTPUT: %s" % (output))

    elif stype == SECTION_COORD:
        if slen == 16:
            output = struct.unpack("<dd", data[offset + 8: (offset + 8 + slen)])

            x_coord = output[0]
            y_coord = output[1]

            if (x_coord > 180) or (x_coord < -180) or (y_coord > 180) or (y_coord < -180):
                bork("BAD COORDS")
            else:
                print("COORDS OUTPUT: %s" % str(output))
        else:
            bork("WRONG SIZE FOR COORDS")

    elif stype == SECTION_REFERENCE:
        if slen == 4:
            output = struct.unpack("<L", data[offset + 8: (offset + 8 + slen)])
            print("REFRENCE OUTPUT: %d" % output[0])
        else:
            bork("WORNG SIZE FOR REFRENCE")
            
    elif stype == SECTION_PNG:
        frmt_str = "<" + ("%s" % 'B' * (slen))
        png_magic = [137, 80, 78, 71, 13, 10, 26, 10]
        output = struct.unpack(frmt_str, data[offset + 8: (offset + 8 + slen)])

        png = png_magic + list(output)

        proc_image_gif("extracted_png", "png", bytearray(png))
        
    elif stype == SECTION_GIF87:
        frmt_str = "<" + ("%s" % 'B' * (slen))
        gif87_magic = [47, 49, 46, 38, 37, 61]
        output = struct.unpack(frmt_str, data[offset + 8: (offset + 8 + slen)])

        gif87 = gif87_magic + list(output)

        proc_image_gif("extracted_gif87", "gif", bytearray(gif87))
        
        
    elif stype == SECTION_GIF89:
        frmt_str = "<" + ("%s" % 'B' * (slen))
        gif89_magic = [47, 49, 46, 38, 39, 61]
        output = struct.unpack(frmt_str, data[offset + 8: (offset + 8 + slen)])

        gif89 = gif87_magic + list(output)

        proc_image_gif("extracted_gif89", "gif", bytearray(gif89))
        
        
    offset = offset + slen + 8
    i = i + 1



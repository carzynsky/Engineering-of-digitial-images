#!/usr/bin/env python3
import numpy
import struct
import zlib

# Image data
image = numpy.array([], dtype=numpy.uint8)

# black => blue
for x in range(255):
    image = numpy.append(image,numpy.array([0,0,x]))

# blue => cyan
for x in range(255):
    image = numpy.append(image,numpy.array([0,x,255]))

# cyan => green
for x in range(255):
    image = numpy.append(image,numpy.array([0,255,255-x]))

# green => yellow
for x in range(255):
    image = numpy.append(image,numpy.array([x,255,0]))

# yellow => red
for x in range(255):
    image = numpy.append(image,numpy.array([255,255-x,0]))

# red => purple
for x in range(255):
    image = numpy.append(image,numpy.array([255,0,x]))

# purple => white
for x in range(255):
    image = numpy.append(image,numpy.array([255,x,255]))

image = numpy.append(image,numpy.array([255,255,255]))

image = [image for x in range (50)]
image = numpy.array(image, dtype=numpy.uint8)

# Construct signature
png_file_signature = b'\x89PNG\r\n\x1a\n'

# Construct header
header_id = b'IHDR'
header_content = struct.pack('!IIBBBBB',1786, 50, 8, 2, 0, 0, 0)
header_size = struct.pack('!I', len(header_content))
header_crc = struct.pack('!I', zlib.crc32(header_id + header_content))
png_file_header = header_size + header_id + header_content + header_crc

# Construct data
data_id = b'IDAT'
data_content = zlib.compress(b''.join(b'\x00' + x.tobytes() for x in image))
data_size = struct.pack('!I', len(data_content))
data_crc = struct.pack('!I', zlib.crc32(data_id + data_content))
png_file_data = data_size + data_id + data_content + data_crc

# Consruct end
end_id = b'IEND'
end_content = b''
end_size = struct.pack('!I', len(end_content))
end_crc = struct.pack('!I', zlib.crc32(end_id + end_content))
png_file_end = end_size + end_id + end_content + end_crc

# Save the PNG image as a binary file
with open('lab4.png', 'wb') as fh:
    fh.write(png_file_signature)
    fh.write(png_file_header)
    fh.write(png_file_data)
    fh.write(png_file_end)
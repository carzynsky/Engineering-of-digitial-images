#!/usr/bin/env python3
import numpy

# PPM file header
ppm_ascii_header = f'P3 1786 50 255 '
ppm_binary_header = f'P6 1786 50 255 '

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

# Save the PPM image as an ASCII file
with open('lab4-ascii.ppm', 'w') as fh:
    fh.write(ppm_ascii_header)
    image.tofile(fh, ' ')

#Save the PPM image as a binary file
with open('lab4-binary.ppm', 'wb') as fh:
    fh.write(bytearray(ppm_binary_header, 'ascii'))
    image.tofile(fh)

#!/usr/bin/env python3
import numpy
#import lab4_utils

# 0. Image data

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

# image = [image for x in range (50)]
image = numpy.array(image, dtype=numpy.uint8)


# 1. Convert RGB to YCbCr


# 2. Downsampling on Cb Cr
# TODO: implement

# 3. Produce 8x8 blocks
# TODO: implement

# 4. Calculate DCT on each block
# TODO: implement

# 5. Divide each block by quantisation matrix
# TODO: implement

# 6. Round each block to integers
# TODO: implement

# 7. Zig Zag
# TODO: implement

# 8. Flatten, concatenate, compress and calculate the size -- how many bytes?
# TODO: implement

# 7'. Undo Zig Zag
# We can skip it in this exercise!

# 6'. Nothing to do here   ¯\_(ツ)_/¯
# For the next step, just reuse the rounded data obtained in step 6.

# 5'. Reverse division by quantisation matrix -- multiply
# TODO: implement

# 4'. Reverse DCT
# TODO: implement

# 3'. Combine 8x8 blocks to original image
# TODO: implement

# 2'. Upsampling on Cb Cr
# TODO: implement

# 1'. Convert YCbCr to RGB
# TODO: implement

# 0'. Save the decoded image -- as PPM or PNG
# TODO: implement

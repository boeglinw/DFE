#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 10:14:13 2021

to create the final iconset do

iconutil -c icns ./Icons.iconset

@author: boeglinw
"""
import numpy as np
from skimage import io, img_as_ubyte
from skimage.transform import resize

im_size = [2**i for i in range(4,11)]

im_large = io.imread('icon_main_large.png')
im_small = io.imread('icon_main_small.png')

output_dir = './Icons.iconset/'

images = []

s_small = 32

for s in im_size:
    if s > s_small:
        images.append(resize(im_large, (s,s), anti_aliasing=True) )
    else:
        images.append(resize(im_small, (s,s), anti_aliasing=True) )


# make output files
# skip the largest size
for i,s in enumerate(im_size[:-1]):
    s2 = im_size[i+1]
    f = output_dir + f'icon_{s}x{s}.png'
    f_x2 = output_dir + f'icon_{s}x{s}@2x.png'
    # save the imahes
    io.imsave(f, img_as_ubyte(images[i]))
    io.imsave(f_x2, img_as_ubyte(images[i+1]))
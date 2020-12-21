#!/usr/bin/env python

from img2vec_pytorch import Img2Vec
from PIL import Image
import glob

image_list = []
for filename in glob.glob('test/*.png'):
    im=Image.open(filename)
    image_list.append(im)

vectors = img2vec.get_vec(image_list)

print("running correctly")

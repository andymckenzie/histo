#!/usr/bin/python3

from img2vec_pytorch import Img2Vec
from PIL import Image
import glob

image_list = []
for filename in glob.glob('test/*.png'):
    im=Image.open(filename)
    image_list.append(im)

# looks like lists are not working
# https://stackoverflow.com/questions/52958116/how-to-write-feature-vectors-for-all-images-of-a-folder-in-a-txt-file-for-future

vectors = Img2Vec.get_vec(image_list)

print("running correctly")

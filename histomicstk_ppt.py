


import large_image
%matplotlib inline
import matplotlib.pyplot as plt
import skimage.io

#Some nice default configuration for plots
plt.rcParams['figure.figsize'] = 15, 15
plt.rcParams['image.cmap'] = 'gray'

# Import and alias positive_pixel_count
import histomicstk.segmentation.positive_pixel_count as ppc


slide_path = '/sc/arion/projects/tauomics/PART_images/Hippocampus_AT8_stain/46974.svs'

ts = large_image.getTileSource(slide_path)

region = dict(
    left=50000, top=35000,
    width=1600, height=900,
)

im_region = ts.getRegion(region=region, format=large_image.tilesource.TILE_FORMAT_NUMPY)[0]

print("The region")
plt.imshow(im_region)
plt.show()

Sandbox for histology analysis. Especially digital whole slide image (wsi) analysis.

# Important Note

Publicly in development. Does not work yet. Do not expect this to work.

# Example tiling on TCGA data

Downloaded the TCGA data using the download data transfer tool available at: https://docs.gdc.cancer.gov/Data_Transfer_Tool/Users_Guide/Getting_Started/



## TCGA data

Downloaded example WSI GBM data from [TCGA](https://portal.gdc.cancer.gov/legacy-archive/search/f?filters=%7B%22op%22:%22and%22,%22content%22:%5B%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22files.data_format%22,%22value%22:%5B%22SVS%22%5D%7D%7D,%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22cases.project.primary_site%22,%22value%22:%5B%22Brain%22%5D%7D%7D%5D%7D).

/Users/mckena01/Documents/histo/gdc-client download -m /home/crary1/Desktop/histo/gdc_manifest.2020-12-28_gbm_top_10.txt

https://portal.gdc.cancer.gov/repository?cases_sort=%5B%7B%22field%22%3A%22primary_site%22%2C%22order%22%3A%22asc%22%7D%5D&facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22brain%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22files.data_type%22%2C%22value%22%3A%5B%22Slide%20Image%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22files.experimental_strategy%22%2C%22value%22%3A%5B%22Diagnostic%20Slide%22%5D%7D%7D%5D%7D&searchTableTab=cases

### Ubuntu download

/home/crary1/Desktop/gdc-client download -m /home/crary1/Desktop/histo/gdc_manifest.2020-12-28_gbm_top_10.txt

## PyHIST

Using [PyHist](https://github.com/manuel-munoz-aguirre/PyHIST#usescript).

Set directory variables for TCGA data. The folder of the images needs to be renamed to "images."

mydir='SET_DIRECTORY_NAME_HERE'

fulldir=$my_dir'gdc_download_20201221_170103.568162/images/'

docker run -v $fulldir:/pyhist/images/ mmunozag/pyhist --save-tilecrossed-image --output images/ images/TCGA-28-1751-01A-01-BS1.71120b58-ac86-4c99-bf81-73d8c08ac74d.svs

docker run -v $fulldir:/pyhist/images/ mmunozag/pyhist --npatches 10 --save-patches --output images/ images/TCGA-28-1751-01A-01-BS1.71120b58-ac86-4c99-bf81-73d8c08ac74d.svs

docker run -v /Volumes/My_Passport_for_Mac/tcga/images/:/pyhist/images/ mmunozag/pyhist --save-tilecrossed-image --npatches 20 --method "otsu" --patch-size 1024 --save-patches --output-downsample 1 --output images/ images/TCGA-CS-6186-01Z-00-DX1.0CF5363F-B6E6-459C-93FD-0BE69F18A51B.svs

FYI: this takes a 346 MB SVS file and turns it into a 2.56 GB folder of .png images. It won't be the same ratio for each .svs image, because it depends on how much of the slide has enough tissue on it. The content threshold default is 0.5.

### Ubuntu

docker run -v /home/crary1/Desktop/histo/tcga/images/:/pyhist/images/ mmunozag/pyhist --save-tilecrossed-image --npatches 20 --method "otsu" --patch-size 1024 --save-patches --output-downsample 1 --output images/ images/TCGA-CS-6186-01Z-00-DX1.0CF5363F-B6E6-459C-93FD-0BE69F18A51B.svs

grant permission to use

sudo chmod -R a+rwx /home/crary1/Desktop/histo/tcga/images/TCGA-CS-6186-01Z-00-DX1.0CF5363F-B6E6-459C-93FD-0BE69F18A51B/TCGA-CS-6186-01Z-00-DX1.0CF5363F-B6E6-459C-93FD-0BE69F18A51B_tiles

# Converting data to TFRecords

sudo apt-get install nvidia-docker -- need to run something equivalent 

https://github.com/jeffheaton/docker-stylegan2-ada

there is a dockerfile to run this: https://github.com/jeffheaton/docker-stylegan2-ada
nvidia-docker run -it -u $(id -u):$(id -g) -v /home/crary1/Desktop/histo/tcga/images/:/mnt heatonresearch/stylegan2-ada /bin/bash

"The following command converts a data set named "fish". The source JPEGs should be in the /mnt/data/fish and the resulting TFRecords will be written to /mnt/datasets/fish."
cd /home/stylegan2-ada/
python dataset_tool.py create_from_images /mnt/tfr/tcga /mnt/TCGA-CS-6186-01Z-00-DX1.0CF5363F-B6E6-459C-93FD-0BE69F18A51B/TCGA-CS-6186-01Z-00-DX1.0CF5363F-B6E6-459C-93FD-0BE69F18A51B_tiles


# img2vec

docker build . --tag img2vecdocker
docker run -ti --name img2vecdocker

## Python script to use pre-trained network to vectorize image

# Trimmed Tiny ImageNet Data

Downloaded via wget http://cs231n.stanford.edu/tiny-imagenet-200.zip.

Trimmed many of the images from the test, train, and val data sets to keep the file size down.

/Users/mckena01/Documents/histo/tiny-imagenet-200/train/n01443537/images/n01443537_0.JPEG



# StyleGan2-ada

https://github.com/NVlabs/stylegan2-ada

docker build --tag stylegan2ada:latest .

Sandbox for histology analysis. Especially digital whole slide image (wsi) analysis.

# Example tiling on TGCA data

## TGCA data

Downloaded example WSI GBM data from [TGCA](https://portal.gdc.cancer.gov/legacy-archive/search/f?filters=%7B%22op%22:%22and%22,%22content%22:%5B%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22files.data_format%22,%22value%22:%5B%22SVS%22%5D%7D%7D,%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22cases.project.primary_site%22,%22value%22:%5B%22Brain%22%5D%7D%7D%5D%7D).

## PyHIST

Using [PyHist](https://github.com/manuel-munoz-aguirre/PyHIST#usescript).

docker run -v /home/crary1/Desktop/histo/data/gdc_download_20201221_170103.568162/images/:/pyhist/images/ mmunozag/pyhist --save-tilecrossed-image --output images/ images/TCGA-28-1751-01A-01-BS1.71120b58-ac86-4c99-bf81-73d8c08ac74d.svs

docker run -v /home/crary1/Desktop/histo/data/gdc_download_20201221_170103.568162/images/:/pyhist/images/ mmunozag/pyhist --npatches 10 --save-patches --output images/ images/TCGA-28-1751-01A-01-BS1.71120b58-ac86-4c99-bf81-73d8c08ac74d.svs

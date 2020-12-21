FROM nvidia/cuda:11.1-base-ubuntu20.04

RUN apt-get update && apt-get install -y \
    software-properties-common
RUN add-apt-repository universe
RUN apt-get update && apt-get install -y \
    apache2 \
    curl \
    git \
    python3.8 \
    python3-pip

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD ./requirements.txt /usr/src/app/requirements.txt
ADD ./hist_img2vec.py /usr/src/app/hist_img2vec.py
ADD ./test /usr/src/app

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

CMD ["hist_img2vec.py"]

ENTRYPOINT [ "./hist_img2vec.py" ]

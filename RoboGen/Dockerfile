
#--------------------------------------------------------------------
# Base Python version 2.7-alpine and 3.6-slim-stretch
# For 2.7-alpine use "apk update/add"
# For 3.6-slim-stretch: use "apt-get update/install"
#--------------------------------------------------------------------
FROM python:3.6-slim-stretch

#--------------------------------------------------------------------
# install dlib
#--------------------------------------------------------------------
RUN apt-get -y update
RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN cd ~ && \
    mkdir -p dlib && \
    git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python3 setup.py install --yes USE_AVX_INSTRUCTIONS

#--------------------------------------------------------------------
# Environment Variables, Directories, ...
#--------------------------------------------------------------------
ARG proxy
ENV https_proxy=$proxy \
	LANG=C.UTF-8 \
	LC_ALL=C.UTF-8
	#LANG=en_US.UTF-8 \
	#LC_ALL=en_US.UTF-8
	
COPY src /root/apps/
WORKDIR /root/apps/
RUN cd /root/apps/

#--------------------------------------------------------------------
# install pipenv and call bootstrap.sh
#--------------------------------------------------------------------
RUN python -V
RUN pip install pipenv && pipenv --python 2.7 install
CMD ["sh","bootstrap.sh"]



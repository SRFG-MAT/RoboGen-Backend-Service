
#--------------------------------------------------------------------
# Base Python version alpine and Co.
# For alpine use "apk update/add" instead of "apt-get update/install"
#--------------------------------------------------------------------
FROM python:2.7.16-alpine
ARG proxy
ENV https_proxy=$proxy \
	LANG=en_US.UTF-8 \
	LC_ALL=en_US.UTF-8
COPY src /apps
WORKDIR /apps

#--------------------------------------------------------------------
# install basic python and pip
#--------------------------------------------------------------------
RUN python -V
RUN pip install pipenv && pipenv install

#--------------------------------------------------------------------
# install dlib
#--------------------------------------------------------------------
RUN apk update 

RUN apk add cmake
#RUN python -m pip install --upgrade pip

RUN pip install scikit-build
#RUN pip install cmake
#RUN pip install dlib


#RUN apk add \
#    build-essential \
#    cmake \
#    gfortran \
#    git \
#    wget \
#    curl \
#    graphicsmagick \
#    libgraphicsmagick1-dev \
#    libatlas-dev \
#    libavcodec-dev \
#    libavformat-dev \
#    libboost-all-dev \
#    libgtk2.0-dev \
#    libjpeg-dev \
#    liblapack-dev \
#    libswscale-dev \
#    pkg-config \
#    python-dev \
#    python-numpy \
#    python-protobuf\
#    software-properties-common \
#    zip \
#RUN apk del -rf /tmp/* /var/tmp/*



#--------------------------------------------------------------------
# call bootstrap.sh
#--------------------------------------------------------------------
CMD ["sh","/apps/bootstrap.sh"]


#--------------------------------------------------------------------
# Base Python version and Co.
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
# install apt-get
#--------------------------------------------------------------------
#RUN wget http://security.ubuntu.com/ubuntu/pool/main/a/apt/apt_1.4_amd64.deb
#RUN sudo dpkg -i apt_1.4_amd64.deb

#--------------------------------------------------------------------
# install dlib
#--------------------------------------------------------------------
#RUN apt-get update && apt-get install -y libopencv-dev
#RUN apt-get update && apt-get -y install cmake protobuf-compiler
#RUN pip install dlib


CMD ["sh","/apps/bootstrap.sh"]

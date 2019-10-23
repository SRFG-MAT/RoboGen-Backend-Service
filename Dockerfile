
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
#RUN pip install numpy
#RUN pip install dlib

#--------------------------------------------------------------------
# call bootstrap.sh
#--------------------------------------------------------------------
CMD ["sh","/apps/bootstrap.sh"]

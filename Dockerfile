FROM python:2.7.16-alpine
ARG proxy
ENV https_proxy=$proxy \
	LANG=en_US.UTF-8 \
	LC_ALL=en_US.UTF-8
COPY src /apps
WORKDIR /apps
RUN python -V
RUN pip install pipenv && pipenv install
RUN pip install dlib
CMD ["sh","/apps/bootstrap.sh"]

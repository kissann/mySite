FROM python:3.7
RUN mkdir src/
WORKDIR /src/
RUN pip install django
ADD . /src/
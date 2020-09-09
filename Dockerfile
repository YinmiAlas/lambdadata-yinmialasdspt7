FROM debian

### so logging/io works reliably w/Docker
ENV PYTHONNUNBUFFERED=1

### UTF  python issue for click package (pipenv dependency)
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

###  need to explicitly set this so 'pipenv shell ' works
ENV SHELL=/BIN/BASH

### BASIC PYTHON DEV DEPENDECIES
RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install python3-pip curl -y && \
  pip3 install pipenv \
  pipenv install pandas \ 
  pip3 install -i https://test.pypi.org/simple/ my-lambdadata-yinmialas==2.1

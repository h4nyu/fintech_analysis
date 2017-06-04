FROM python:3.5-slim

MAINTAINER Xinyaun Yao <yao.xinyuan@canon.co.jp>

RUN apt-get update && apt-get install -y \
    gcc \
    make \
    exuberant-ctags \
    graphviz

ARG uid
RUN echo "${user}, ${uid}, ${gid}"
RUN adduser --uid ${uid} --disabled-password app --gecos "" 

RUN pip install pip-tools

WORKDIR /app
ADD ./requirements.txt /app
ADD ./dev-requirements.txt /app
ADD ./Makefile /webapp
RUN make sync_package

ADD ./ /app
RUN pip install -e .[dev]
USER app
CMD ["python", "run.py"]

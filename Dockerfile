FROM python:3.8.0

FROM ubuntu:18.04

RUN apt-get update && apt-get install -y
curl apt-utils apt-transport-https debconf-utils gcc build-essential g++-5
&& rm -rf /var/lib/apt/lists/*

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql unixodbc-dev
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN /bin/bash -c "source ~/.bashrc"

RUN apt-get update && apt-get install -y
python-pip python-dev python-setuptools
--no-install-recommends
&& rm -rf /var/lib/apt/lists/*

RUN apt install python3.8

RUN pip install --upgrade pip

RUN mkdir /main
WORKDIR /main

ADD requirements.txt /main/

RUN pip install -r requirements.txt

ADD . /main/

ENTRYPOINT ["python", "main.py"]
FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv

# update pip
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel

# copy and install requirements and install
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt
RUN rm /opt/app/requirements.txt

# copy application and data into container
COPY data/* /opt/app/data/
COPY myapp/main.py /opt/app/myapp/

# start bokeh application
CMD ["bokeh", "serve", "--show", "myapp/"]


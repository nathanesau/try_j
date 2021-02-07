# debian based docker image
FROM python:3.9

RUN apt-get update
RUN apt-get -y install g++
RUN apt-get -y install libc6 libc6-dev
RUN apt-get -y install git
RUN apt-get -y install ninja-build
RUN apt-get -y install python3-dev

# install latest cmake
RUN pip install cmake --upgrade

# install jconsole
RUN git clone https://github.com/nathanesau/jsource
RUN cd jsource && mkdir build && cmake -G "Ninja" -B /jsource/build && ninja -C build
RUN ln -s /jsource/build/jsrc/jconsole /usr/bin/jconsole

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY config.py ./
COPY j-app.py ./
COPY boot.sh ./

RUN chmod +x boot.sh

ENV FLASK_APP app.py

EXPOSE 80
ENTRYPOINT ["./boot.sh"]
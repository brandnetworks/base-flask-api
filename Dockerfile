FROM debian

ENV LANG C.UTF-8
RUN apt-get update &&\
    apt-get install -y python-pip python-dev libpq-dev &&\
    pip install virtualenv
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt run.py /usr/src/app/
RUN /bin/bash -c "virtualenv venv &&\
    source venv/bin/activate &&\
    pip install -r requirements.txt"
COPY api /usr/src/app/api
RUN /usr/src/app/venv/bin/flake8 $(find /usr/src/app -name '*.py' | grep -v 'venv') &&\
    /usr/src/app/venv/bin/python -m unittest discover
#CMD [ "tar", "-cf", "-", "." ]
CMD [ "venv/bin/gunicorn", "-w", "2", "-b", ":5000", "run:app" ]

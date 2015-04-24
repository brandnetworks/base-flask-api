Base Flask API
==============

Getting Started
---------------

To start development:

```
$ brew install python
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ flake8 $(find . -name '*.py' | grep -v 'venv')
$ python -m unittest discover
```

To get it running, there are two options:

```
$ ./run.py # great for debugging; needs DATABASE_URL to be set
$ docker-compose build && docker-compose up # most like production
```

Then, assuming you are running with Docker, hitting an endpoint is as simple as

```
http $(boot2docker ip):8000/
http $(boot2docker ip):8000/health/
```

Distribution
------------

To build a Docker image for distribution:

```
docker build -t geowa4/base-flask-api .
docker run --rm -it -p 8000:8000 -e 'DATABASE_URI=postgres://' geowa4/base-flask-api
```

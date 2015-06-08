Base Flask API
==============

Getting Started
---------------

To start development:

```
$ brew install python3
$ virtualenv --python=python3 venv
$ source venv/bin/activate
$ make install
$ make test
```

Note: In order to successfully run the `make install` command, you must have PostgreSQL installed on your local machine. On Macs this can be done with the Homebrew command `brew install postgresql`

To get it running, there are two options:

The first runs Postgres in a Docker container and the API locally in debug mode.

```
$ make dev
```

The second runs both Postgres and the API in Docker.
This is most like production.

```
$ make watch
```

Then, assuming you are running with Docker, hitting an endpoint is as simple as

```
http $(boot2docker ip):5000/
http $(boot2docker ip):5000/health/
```

Distribution
------------

To build a Docker image for distribution:

```
docker build -t geowa4/base-flask-api .
docker run --rm -it -p 5000:5000 -e 'DATABASE_URI=postgresql://' geowa4/base-flask-api
```

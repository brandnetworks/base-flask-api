FROM python:3-onbuild

RUN flake8 $(find /usr/src/app -name '*.py' | grep -v 'venv') &&\
    python -m unittest discover
CMD [ "gunicorn", "-w", "2", "-b", ":5000", "run:app" ]

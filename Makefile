SRC_FILES=$(shell find . -name '*.py' | grep -v 'venv')
DOCKER_IP=$(shell boot2docker ip)

all: docker

install:
	pip install -r requirements.txt

lint:
	flake8 $(SRC_FILES)

test: lint
	python -m unittest discover

docker: test
	docker build -t geowa4/base-flask-api .

clean:
	docker-compose kill
	docker-compose rm -f

dev: clean
	docker-compose up -d db
	DATABASE_URI=postgresql://base_api:pwgen_-sny_40@$(DOCKER_IP):5432/postgres \
		./run.py

dev-docker: clean
	docker-compose build
	docker-compose up -d

watch: dev-docker
	watchmedo shell-command \
		--patterns="*.py" \
		--recursive \
		--command='make dev-docker' \
		.

.PHONY: install lint test docker clean dev watch

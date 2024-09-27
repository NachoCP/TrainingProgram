DOCKER_COMPOSE = docker-compose
PYTHON = python3
DATA_DIR = ./data

.PHONY: run stop test lint checks clean

run:
	$(DOCKER_COMPOSE) up -d

stop:
	$(DOCKER_COMPOSE) down
	rm -rf $(DATA_DIR)

test:
	$(PYTHON) -m pytest

lint:
	ruff .

checks:
	ruff check .
	mypy .

clean:
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -rf {} +

DOCKER_COMPOSE = docker-compose
PYTHON = python3
DATA_DIR = ./data
MILVUS_FILE = "milvus_little.db"

.PHONY: run stop test lint checks clean

run:
	$(DOCKER_COMPOSE) up -d

stop:
	$(DOCKER_COMPOSE) down
	rm -rf $(DATA_DIR)

test:
	$(PYTHON) -m pytest
	rm -rf $(MILVUS_FILE)

lint:
	black .

clean:
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -rf {} +

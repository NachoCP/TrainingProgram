NAME := .
POETRY := $(shell command -v poetry 2> /dev/null)
DOCKER_COMPOSE := docker-compose
DATA_DIR := ./data
LOG_DIR := ./logs

.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo ""
	@echo "  install     install packages and prepare environment"
	@echo "  update      update packages and prepare environment"
	@echo "  run         run the docker compose up with all the dependencies"
	@echo "  stop        tear down the docker compose and delete the tmp data directories"
	@echo "  clean       remove all temporary files"
	@echo "  lint        run the code linters"
	@echo "  format      reformat code"
	@echo "  test        run all the tests"
	@echo ""
	@echo "Check the Makefile to know exactly what each target is doing."
    
install:
	@if [ -z $(POETRY) ]; then echo "Poetry could not be found. See https://python-poetry.org/docs/"; exit 2; fi
	$(POETRY) install

update:
	@if [ -z $(POETRY) ]; then echo "Poetry could not be found. See https://python-poetry.org/docs/"; exit 2; fi
	$(POETRY) update

.PHONY: run
run:
	$(DOCKER_COMPOSE) up -d

.PHONY: stop
stop:
	$(DOCKER_COMPOSE) down
	rm -rf $(DATA_DIR)
	rm -rf $(LOG_DIR)

.PHONY: test
test:
	$(POETRY) run pytest ./tests/ --cov-report term-missing --cov-fail-under 80 --cov .

.PHONY: lint
lint:
	$(POETRY) run black --check ./tests/ . --diff
	$(POETRY) run mypy ./tests/ .--ignore-missing-imports

.PHONY: format
format:
	$(POETRY) run isort --profile=black --lines-after-imports=2 ./tests/ .
	$(POETRY) run black ./tests/ .


.PHONY: clean
clean:
	find . -type d -name "__pycache__" | xargs rm -rf {};
	rm -rf .coverage .mypy_cache

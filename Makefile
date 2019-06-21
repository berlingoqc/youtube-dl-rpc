PROJECT_NAME := youtube-dl-rpc
VERSION := $(shell git describe --abbrev=0 --tags)

RELEASE := $(PROJECT_NAME)_$(VERSION).tar.gz

ensure-pip:
	pip install --user --upgrade pipenv pip
	pip --version
	pipenv --version

dep: ensure-pip
	pipenv install --dev
	pipenv sync

all: clean dep build

test: dep
	@echo "Running test"

build:
	@pipenv run pyinstaller --onefile ./main.py 

clean:
	@rm -rf ./build ./dist ./__pycache__
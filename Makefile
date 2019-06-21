PROJECT_NAME := youtube-dl-rpc
VERSION := $(shell git describe --abbrev=0 --tags)

ifeq ($(OS),Windows_NT) 
    detected_OS := windows
else
    detected_OS := linux
endif

RELEASE := $(PROJECT_NAME)_$(VERSION)_$(detected_OS).tar.gz


ensure-pip:
	pip install --user --upgrade pipenv pip
	pip --version
	pipenv --version

dep: ensure-pip
	pipenv install --dev
	pipenv sync

all: clean dep release

test: dep
	@echo "Running test"

build:
	@pipenv run pyinstaller --onefile ./main.py -n $(PROJECT_NAME)

clean:
	@rm -rf ./build ./dist ./__pycache__

release:
	mkdir -p ./release
	tar --transform 's,.*/,,g' -cvf ./release/$(RELEASE) dist/$(PROJECT_NAME) ./config.json

.PHONY: default
default: all

.PHONY: all
all: requirements-base.txt requirements.txt

.PHONY: install
install: requirements-base.txt requirements.txt
	pip-sync $^

requirements.txt: requirements-base.txt

%.txt: %.in
	pip-compile $<

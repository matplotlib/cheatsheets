.PHONY: default
default: all

.PHONY: all
all: requirements.txt

.PHONY: install
install: requirements.txt
	pip-sync $^

%.txt: %.in
	pip-compile $<

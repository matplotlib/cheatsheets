SRC := $(wildcard *.tex)

.PHONY: default
default: all

.PHONY: all
all: figures cheatsheets

.PHONY: figures
figures:
	cd scripts && for script in *.py; do echo $$script; python $$script; done

.PHONY: cheatsheets
cheatsheets:
	xelatex cheatsheets.tex

.PHONY: handouts
handouts:
	# xelatex handout-beginner.tex
	# xelatex handout-intermediate.tex
	xelatex handout-tips.tex

.PHONY: fonts
fonts:
	make -C fonts/

.PHONY: clean
clean: $(SRC)
	git clean -f ./figures/
	git clean -f ./scripts/*.pdf
	latexmk -c $^

.PHONY: requirements
requirements:
	$(MAKE) -C ./requirements/

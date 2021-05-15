SRC := $(wildcard *.tex)

.PHONY: default
default: all

.PHONY: all
all: logos figures cheatsheets handouts

.PHONY: logos
logos:
	cd logos && python mpl-logos2.py && pdfcrop mpl-logo2.pdf mpl-logo2.pdf

.PHONY: figures
figures:
	# generate the figures
	cd scripts && for script in *.py; do echo $$script; python $$script; done
	# crop the figures
	cd figures && for figure in *.pdf; do echo $$figure; pdfcrop $$figure $$figure; done
	# regenerate some figures that should not be cropped
	cd scripts && python styles.py

.PHONY: cheatsheets
cheatsheets:
	xelatex cheatsheets.tex

.PHONY: handouts
handouts:
	xelatex handout-beginner.tex
	xelatex handout-intermediate.tex
	xelatex handout-tips.tex

.PHONY: fonts
fonts:
	make -C fonts/

.PHONY: clean
clean: $(SRC)
	- rm ./logos/mpl-logo2.pdf
	git clean -f -X ./figures/
	git clean -f ./scripts/*.pdf
	latexmk -c $^

.PHONY: requirements
requirements:
	$(MAKE) -C ./requirements/

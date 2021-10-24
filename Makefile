SRC := $(wildcard *.tex)

.PHONY: default
default: all

.PHONY: all
all: logos figures cheatsheets handouts
	mkdir -p ./build/
	cp cheatsheets*.p* ./build/
	cp handout-*.p* ./build/

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
	convert -density 150 cheatsheets.pdf -scene 1 cheatsheets.png

.PHONY: handouts
handouts:
	xelatex handout-beginner.tex
	xelatex handout-intermediate.tex
	xelatex handout-tips.tex
	convert -density 150 handout-tips.pdf handout-tips.png
	convert -density 150 handout-beginner.pdf handout-beginner.png
	convert -density 150 handout-intermediate.pdf handout-intermediate.png

.PHONY: check
check:
	./check-layout.sh cheatsheets.pdf 2
	./check-layout.sh handout-tips.pdf 1
	./check-layout.sh handout-beginner.pdf 1
	./check-layout.sh handout-intermediate.pdf 1
	./check-links.py cheatsheets.pdf

.PHONY: fonts
fonts:
	make -C fonts/

.PHONY: clean
clean: $(SRC)
	latexmk -c $^
	- rm -rf ./build/

.PHONY: clean-all
clean-all: clean
	- rm ./logos/mpl-logo2.pdf
	git clean -f -X ./figures/
	git clean -f ./scripts/*.pdf

.PHONY: requirements
requirements:
	$(MAKE) -C ./requirements/

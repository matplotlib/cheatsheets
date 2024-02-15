SRC := $(wildcard *.tex)
CONVERTFLAGS = -density 150 -alpha remove -depth 8

.PHONY: default
default: all

.PHONY: all
all: logos figures cheatsheets handouts docs

.PHONY: logos
logos:
	wget https://github.com/matplotlib/matplotlib/raw/v3.7.4/doc/_static/logo2.png -O ./logos/logo2.png

.PHONY: figures
figures:
	# generate the figures
	cd scripts && for script in *.py; do echo $$script; MPLBACKEND="agg" python $$script; done
	# crop some of the figures
	cd figures && pdfcrop adjustments.pdf adjustments.pdf
	cd figures && pdfcrop annotate.pdf annotate.pdf
	cd figures && pdfcrop annotation-arrow-styles.pdf annotation-arrow-styles.pdf
	cd figures && pdfcrop anatomy.pdf anatomy.pdf
	cd figures && pdfcrop colornames.pdf colornames.pdf
	cd figures && pdfcrop fonts.pdf fonts.pdf
	cd figures && pdfcrop markers.pdf markers.pdf
	cd figures && pdfcrop text-alignments.pdf text-alignments.pdf
	cd figures && pdfcrop tick-formatters.pdf tick-formatters.pdf
	cd figures && pdfcrop tick-locators.pdf tick-locators.pdf
	cd figures && pdfcrop tip-font-family.pdf tip-font-family.pdf
	cd figures && pdfcrop tip-hatched.pdf tip-hatched.pdf

.PHONY: cheatsheets
cheatsheets:
	xelatex cheatsheets.tex
	convert $(CONVERTFLAGS) cheatsheets.pdf -scene 1 cheatsheets.png

.PHONY: handouts
handouts:
	xelatex handout-beginner.tex
	xelatex handout-intermediate.tex
	xelatex handout-tips.tex
	convert $(CONVERTFLAGS) handout-tips.pdf handout-tips.png
	convert $(CONVERTFLAGS) handout-beginner.pdf handout-beginner.png
	convert $(CONVERTFLAGS) handout-intermediate.pdf handout-intermediate.png

.PHONY: check
check:
	./check-matplotlib-version.py
	./check-num-pages.sh cheatsheets.pdf 2
	./check-num-pages.sh handout-tips.pdf 1
	./check-num-pages.sh handout-beginner.pdf 1
	./check-num-pages.sh handout-intermediate.pdf 1
	./check-diffs.py
	./check-links.py cheatsheets.pdf

.PHONY: docs
docs:
	make -C docs/ html
	cp ./cheatsheets*.p* ./docs/_build/html
	cp ./handout-*.p* ./docs/_build/html


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

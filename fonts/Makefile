FONT_DIRS := eb-garamond roboto roboto-mono roboto-slab source-code-pro source-sans-pro source-serif-pro

EB_GARAMOND_ZIP      := https://bitbucket.org/georgd/eb-garamond/downloads/EBGaramond-0.016.zip
ROBOTO_ZIP           := https://github.com/googlefonts/roboto/releases/download/v2.138/roboto-unhinted.zip
ROBOTO_MONO_ZIP      := https://github.com/googlefonts/RobotoMono/archive/8f651634e746da6df6c2c0be73255721d24f2372.zip
ROBOTO_SLAB_ZIP      := https://github.com/googlefonts/robotoslab/archive/a65e6d00d8e3e7ee2fabef844e58fa12690384d2.zip
SOURCE_CODE_PRO_ZIP  := https://github.com/adobe-fonts/source-code-pro/releases/download/2.038R-ro%2F1.058R-it%2F1.018R-VAR/OTF-source-code-pro-2.038R-ro-1.058R-it.zip
SOURCE_SANS_PRO_ZIP  := https://github.com/adobe-fonts/source-sans/releases/download/2.045R-ro%2F1.095R-it/source-sans-pro-2.045R-ro-1.095R-it.zip
SOURCE_SERIF_PRO_ZIP := https://github.com/adobe-fonts/source-serif/releases/download/3.001R/source-serif-pro-3.001R.zip

UNZIP_FLAGS := -x "__MACOSX/*"


.PHONY: default
default: all

.PHONY: all
all: sources
	mkdir -p $(FONT_DIRS)
	cd eb-garamond && unzip -j /tmp/eb-garamond.zip "EBGaramond-0.016/otf/*.otf" $(UNZIP_FLAGS)
	cd roboto && unzip -j /tmp/roboto.zip "*.ttf" $(UNZIP_FLAGS)
	cd roboto-mono && unzip -j /tmp/roboto-mono.zip "RobotoMono-8f651634e746da6df6c2c0be73255721d24f2372/fonts/ttf/*.ttf" $(UNZIP_FLAGS)
	cd roboto-slab && unzip -j /tmp/roboto-slab.zip "robotoslab-a65e6d00d8e3e7ee2fabef844e58fa12690384d2/fonts/static/*.ttf" $(UNZIP_FLAGS)
	cd source-code-pro && unzip -j /tmp/source-code-pro.zip "*.otf" $(UNZIP_FLAGS)
	cd source-sans-pro && unzip -j /tmp/source-sans-pro.zip "source-sans-pro-2.045R-ro-1.095R-it/OTF/*.otf" $(UNZIP_FLAGS)
	cd source-serif-pro && unzip -j /tmp/source-serif-pro.zip "source-serif-pro-3.001R/OTF/*.otf" $(UNZIP_FLAGS)

.PHONY: sources
sources:
	wget $(EB_GARAMOND_ZIP) -O /tmp/eb-garamond.zip
	wget $(ROBOTO_ZIP) -O /tmp/roboto.zip
	wget $(ROBOTO_MONO_ZIP) -O /tmp/roboto-mono.zip
	wget $(ROBOTO_SLAB_ZIP) -O /tmp/roboto-slab.zip
	wget $(SOURCE_CODE_PRO_ZIP) -O /tmp/source-code-pro.zip
	wget $(SOURCE_SANS_PRO_ZIP) -O /tmp/source-sans-pro.zip
	wget $(SOURCE_SERIF_PRO_ZIP) -O /tmp/source-serif-pro.zip

.PHONY: clean
clean:
	- rm $(HOME)/.cache/matplotlib/fontlist*
	- rm -rf $(FONT_DIRS)

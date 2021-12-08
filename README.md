# Cheatsheets for Matplotlib users

## Cheatsheets
Cheatsheet [(download pdf)](https://matplotlib.org/cheatsheets/cheatsheets.pdf) | |
:------------------------------------------------------------------------------:|:----------------------------------------------------------:
![](https://matplotlib.org/cheatsheets/cheatsheets-1.png)                       | ![](https://matplotlib.org/cheatsheets/cheatsheets-2.png)

## Handouts

Beginner handout [(download pdf)](https://matplotlib.org/cheatsheets/handout-beginner.pdf) | Intermediate handout [(download pdf)](https://matplotlib.org/cheatsheets/handout-intermediate.pdf) | Tips handout [(download pdf)](https://matplotlib.org/cheatsheets/handout-tips.pdf)
:-----------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:
![](https://matplotlib.org/cheatsheets/handout-beginner.png)                               | ![](https://matplotlib.org/cheatsheets/handout-intermediate.png)                                   | ![](https://matplotlib.org/cheatsheets/handout-tips.png)

# For contributors to the cheatsheets

## How to compile

1. You need to create a `fonts` repository with:

* `fonts/roboto/*`           : See https://fonts.google.com/specimen/Roboto
                                or https://github.com/googlefonts/roboto/tree/master/src/hinted
* `fonts/roboto-slab/*`      : See https://fonts.google.com/specimen/Roboto+Slab
                                or https://github.com/googlefonts/robotoslab/tree/master/fonts/static
* `fonts/source-code-pro/*`  : See https://fonts.google.com/specimen/Source+Code+Pro
                                or https://github.com/adobe-fonts/source-code-pro/tree/release/OTF
* `fonts/source-sans-pro/*`  : See https://fonts.google.com/specimen/Source+Sans+Pro
                                or https://github.com/adobe-fonts/source-sans-pro/tree/release/OTF
* `fonts/source-serif-pro/*` : See https://fonts.google.com/specimen/Source+Serif+Pro
                                or https://github.com/adobe-fonts/source-serif-pro/tree/release/OTF
* `fonts/eb-garamond/*`      : See https://bitbucket.org/georgd/eb-garamond/src/master
* `fonts/pacifico/*`         : See https://fonts.google.com/download?family=Pacifico

On Linux, with `make` installed, the fonts can be set up with the following command:
```shell
make -C fonts
```

The fonts can be made discoverable by `matplotlib` (through `fontconfig`) by creating the following in `$HOME/.config/fontconfig/fonts.conf` (see [here](https://www.freedesktop.org/software/fontconfig/fontconfig-user.html)):

```xml
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
<dir>/path/to/cheatsheets/fonts/</dir>
...
</fontconfig>
```


2. You need to generate all the figures:

```
$ cd scripts
$ for script in *.py; do python $script; done
$ cd ..
```

3. Compile the sheet
```
$ xelatex cheatsheets.tex
$ xelatex cheatsheets.tex
```

# cheatsheets
Various cheat sheets for matplotlib

# How to compile

1. You need to create a `fonts` repository with:

* `fonts/roboto/*`           : See https://fonts.google.com/specimen/Roboto
* `fonts/source-code-pro/*`  : See https://fonts.google.com/specimen/Source+Code+Pro
* `fonts/source-sans-pro/*`  : See https://fonts.google.com/specimen/Source+Sans+Pro
* `fonts/source-serif-pro/*` : See https://fonts.google.com/specimen/Source+Serif+Pro

2. You need to generate all the figures:

```
$ cd scripts
$ for script in *.py; do python $script; done
$ cd ..
```

3. Compile the sheet
```
$ xelatex cheatsheet-basic.tex
$ xelatex cheatsheet-basic.tex
```




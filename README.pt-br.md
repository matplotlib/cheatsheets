# Folhas de dicas para usuários do Matplotlib

## Observação
O conteúdo original dessa folha de dicas é do repositório [oficial do
`matplotlib`](https://github.com/matplotlib/cheatsheets). Essa tradução
não-oficial visa tornar as dicas mais acessíveis para pessoas que usam a Matplotlib.

Façam bom uso!

## Folhas de dicas
Cheatsheet [(baixe o pdf)](https://matplotlib.org/cheatsheets/cheatsheets.pdf) | |
:------------------------------------------------------------------------------:|:----------------------------------------------------------:
![](https://matplotlib.org/cheatsheets/cheatsheets-1.png)                       | ![](https://matplotlib.org/cheatsheets/cheatsheets-2.png)

## Folhetos

Folheto iniciante [(download pdf)](https://matplotlib.org/cheatsheets/handout-beginner.pdf) | Folheto intermediário [(download pdf)](https://matplotlib.org/cheatsheets/handout-intermediate.pdf) | Folheto de dicas [(download pdf)](https://matplotlib.org/cheatsheets/handout-tips.pdf)
:-----------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:
![](https://matplotlib.org/cheatsheets/handout-beginner.png)                               | ![](https://matplotlib.org/cheatsheets/handout-intermediate.png)                                   | ![](https://matplotlib.org/cheatsheets/handout-tips.png)

# Para contribuidores das dicas

## Como compilar

1. Você precisa criar um repositório `fonts` com:

* `fonts/roboto/*`           : Veja https://fonts.google.com/specimen/Roboto
                                ou https://github.com/googlefonts/roboto/tree/master/src/hinted
* `fonts/roboto-slab/*`      : Veja https://fonts.google.com/specimen/Roboto+Slab
                                ou https://github.com/googlefonts/robotoslab/tree/master/fonts/static
* `fonts/source-code-pro/*`  : Veja https://fonts.google.com/specimen/Source+Code+Pro
                                ou https://github.com/adobe-fonts/source-code-pro/tree/release/OTF
* `fonts/source-sans-pro/*`  : Veja https://fonts.google.com/specimen/Source+Sans+Pro
                                ou https://github.com/adobe-fonts/source-sans-pro/tree/release/OTF
* `fonts/source-serif-pro/*` : Veja https://fonts.google.com/specimen/Source+Serif+Pro
                                ou https://github.com/adobe-fonts/source-serif-pro/tree/release/OTF
* `fonts/eb-garamond/*`      : Veja https://bitbucket.org/georgd/eb-garamond/src/master
* `fonts/pacifico/*`         : Veja https://fonts.google.com/download?family=Pacifico

No Linux, com o `make` instalado, as fontes podem ser configuradas com o seguinte comando:

```shell
make -C fonts
```

As fontes podem ser descobertas pelo `matplotlib` (por via do `fontconfig`) ao
criar o arquivo `$HOME/.config/fontconfig/fonts.conf` com o seguinte conteúdo (veja [aqui](https://www.freedesktop.org/software/fontconfig/fontconfig-user.html)):

```xml
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
<dir>/path/to/cheatsheets/fonts/</dir>
...
</fontconfig>
```


2. Você precisa gerar todas as figuras:

```
$ cd scripts
$ for script in *.py; do python $script; done
$ cd ..
```

3. Compile a folha
```
$ xelatex cheatsheets.tex
$ xelatex cheatsheets.tex
```

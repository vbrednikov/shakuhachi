Shakuhachi notes help script
============================

I am learning to play shakuhachi and my zen-guru gave me the task: write multiple
small random sequences of notes (ro - tsu - re - chi - ri - i) in katakana and play
them in written order, to get familiar with the names and symbols.

Instead of this, I spent several hours automating it with python and latex.

## Python script

Python script `shaku.py` is pretty simple. Without arguments, it just generates 15 random
pairs (vertical RTL alignment is TBD, but it's ok to play it in this manner):

```
$ ./shaku.py
リ ツ
ハ ツ
ハ リ
レ レ
リ チ
ロ ロ
ロ ツ
リ ロ
チ リ
チ チ
チ レ
ハ リ
ハ ツ
ハ ロ
チ ロ
```

It also accepts some parameters: -n is number of sequences and -c is number of
notes in a sequences.
```
$ ./shaku.py -n 5 -c 4
ロ チ リ ツ
ハ ロ ツ リ
ツ レ チ チ
ツ レ チ リ
ロ リ ハ チ
```

It also  can write names instead if symbols:
```
$ ./shaku.py -n 3 -c 7 --names
i   i   i   re  tsu ro  re
tsu chi re  ro  ri  tsu ri
i   ri  i   ro  re  tsu ro
```

## Xetex/Latex

To generate PDF with japanese text, I prepared a docker image

To build the image with xetex and some [Google free Noto fonts](https://www.google.com/get/noto/) [for CJK](https://github.com/googlei18n/noto-cjk) onboard:

```
$ docker build -t vbrednikov/jxelatex .
```

To run `xelatex` from inside the image with sample tex file (original sample taken from [this famous page](https://nablux.net/tgp/weblog/2013/03/22/how-typeset-japanese-using-xelatex/)):

```
$ docker run -v `pwd`:/work --rm vbrednikov/jxelatex:1.0 xelatex example.tex
```

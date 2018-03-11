Shakuhachi notes help script
============================

I am learning to play shakuhachi and my zen-guru gave me the task: write multiple
small random sequences of notes (ro - tsu - re - chi - ri - i) in katakana and play
them in written order, to get familiar with the names and symbols.

Instead of this, I spent several hours automating it with python and latex.

1. Python script is pretty simple. Without arguments, it just generates 15 random
pairs:

```
$ ./shaku.py
```

It also accepts some parameters: -n is number of sequences and -c is number of
notes in a sequences.
```
$ ./shaku.py -n 5 -c 4
TBD
```

It also  can write names instead if symbols:
```
./shaku.py -n 3 -c 7 --names
i   i   i   re  tsu ro  re
tsu chi re  ro  ri  tsu ri
i   ri  i   ro  re  tsu ro
```

#!/usr/bin/env python
# -*- coding: utf -8 -*-
# apt-get install texlive-latex-base texlive-xetex latex-cjk-japanese --no-install-recommends
# http://fontsgeek.com/fonts/Kozuka-Gothic-Pro-M/download
# http://www.exljbris.com/dl/delicious-123.zip

import random
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class ShakuNotes(object):
    """docstring for ShakuNotes"""
    def __init__(self):
        self.notes = {
                'ro' : u"ロ",
                'tsu': u"ツ",
                're' : u"レ",
                'chi': u"チ",
                'ri' : u"リ",
                'i'  : u"ハ",
                }

    def doubles(self, names=False, notes=2, number=15):
        """produce number pairs of random notes"""
        format = "{}"
        if names is True:
            flat = self.notes.keys()
            format = "{:3}"
        else:
            flat = self.notes.values()
        for n in xrange(number):
            indices = [random.choice(range(len(self.notes))) for i in xrange(notes)]
            print ' '.join(format.format(flat[i]) for i in indices)



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Shakuhachi tab tool')
    parser.add_argument('-n', type=int, default=15, help="How many sequences to produce")
    parser.add_argument('-c', type=int, default=2,  help='How many notes in sequence')
    parser.add_argument('--names', action='store_true', default=False,  help='Use notes names instead of representations')


    args = parser.parse_args()
#    print args

    s = ShakuNotes()
    s.doubles(args.names, args.c, args.n)

#-*- coding:utf-8 -*-

import expressions
from expressions import Literal, FuncCall
from ifexp import If


def __make_placeholders():

    for i in range(0, 16):
        exec '_{0} = expressions.Placeholder({1})'.format(i+1, i) in globals()

__make_placeholders()


_k = expressions.PlaceholderMaker()
map = Literal(map)
reduce = Literal(reduce)
filter = Literal(filter)
_v = Literal




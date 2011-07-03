#-*- coding:utf-8 -*-

import expressions
from expressions import Literal, FuncCall
from ifexp import If as if_


def __make_placeholders():

    for i in range(0, 16):
        exec '_{0} = expressions.Placeholder({1})'.format(i+1, i) in globals()

__make_placeholders()


_ = expressions.Placeholder(0)
_k = expressions.PlaceholderMaker()
_v = Literal
map_ = Literal(map)
reduce_ = Literal(reduce)
filter_ = Literal(filter)
list_ = Literal(list)
tuple_ = Literal(tuple)
dict_ = Literal(dict)






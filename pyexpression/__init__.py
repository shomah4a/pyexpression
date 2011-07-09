#-*- coding:utf-8 -*-
'''
boost.lambda like function generator

Usage:

  >>> from pyexpression import _1, _2
  >>> _1 * 10
  <pyexpression.expressions.FuncCall object at 0xb74db7cc>
  >>> (_1 * 10)(5)
  50
  >>> (_1 * _2)(10, 10)
  100
  >>> map(_1[0], zip(range(10), range(10,20)))
  >>> class Test(object):
  ...     def __init__(self):
  ...         self.x = 10
  ...
  >>> (_1.x)(Test())
  10

'''
import expressions
from expressions import Literal, FuncCall
from ifexp import If as if_

__version__ = '0.1.0'
__author__ = 'Shoma Hosaka'
__license__ ='LGPL'



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






#-*- coding:utf-8 -*-

from pyexpression import FuncCall, Literal, _1, _2, _k


def test_expression():
    u'''
    単純式
    '''
    
    assert (Literal(10) * 10).eval() == 100



def test_function():
    u'''
    関数呼び出し
    '''

    @Literal
    def add(x, y):
        return x + y

    assert add(10, 20).eval() == 30

    assert FuncCall(add, 10, 20).eval() == 30
    


def test_getitem():
    u'''
    インデックスアクセス
    '''

    x = Literal([1,2,3])

    assert x[2].eval() == 2



def test_slice():
    u'''
    スライス
    '''

    x = Literal([1,2,3,4,5])

    assert x[0:10:2].eval() == [1,3,5]



def test_placeholder():
    u'''
    引数
    '''
    
    @Literal
    def test(x, y):

        return x + y

    assert(test(_1, 10) + _2 * _k.abc).eval(10, 20, abc=10) == 220



def test_getattr():
    u'''
    getattr してみる
    '''

    class Dummy():

        def __init__(self):

            self.x = 10
            self.y = 20
            self.z = 30


    assert (_1.x + 20)(Dummy()) == 30



def test_complex():
    u'''
    ちょっと複雑
    '''

    @Literal
    def test(x, y):

        return range(x, y)

    assert test(0, y=20)[0,20,5] * 2 == range(0, 20, 10)*2



def test_map():
    u'''
    マップ
    '''

    assert map(_1 + 10, range(10)) == range(10, 20)

    

def test_method():
    u'''
    メソッド
    '''

    class Test(object):
    
        def call(self):

            return 100


    assert (_1._m.call() + 200)(Test()) == 300





#-*- coding:utf-8 -*-


from pyexpression import FuncCall, Literal, _1, _2, _k, if_


def test_if():

    x = Literal(10)

    b = if_(_1)[
        10
        ].elif_(_2)[
        20
        ].else_[
            30
            ]

    assert b.eval(1, 2, 3) == 10
    assert b.eval(0, 2, 3) == 20
    assert b.eval(0, 0, 3) == 30
    


    

#-*- coding:utf-8 -*-

import expressions as exp


class If(object):
    u'''
    if 式
    '''

    def __init__(self, cond, items=[]):

        self.condition = exp.to_expression(cond)
        self.items = items


    def __getitem__(self, block):

        return EvaluableIf(IfBlock(self.condition, exp.to_expression(block)), self.items)



class IfBlock(object):

    def __init__(self, cond, block):

        self.cond = cond
        self.block = block


class EvaluableIf(exp.Expression):
    u'''
    if 式
    '''
    def __init__(self, block, items):

        self.items = items + [block]


    def eval(self, *args, **argd):

        for it in self.items:
            if isinstance(it, IfBlock):
                if it.cond.eval(*args, **argd):
                    return it.block.eval(*args, **argd)
            else:
                return it.eval(*args, **argd)


    def elif_(self, cond):

        return If(cond, self.items)


    @property
    def else_(self):

        return If(True, self.items)
        



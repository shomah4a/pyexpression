#-*- coding:utf-8 -*-


import operator



def to_expression(obj):

    if isinstance(obj, Expression):
        return obj
    elif isinstance(obj, tuple):
        return Tuple(obj)
    elif isinstance(obj, list):
        return List(obj)

    return Literal(obj)



class Expression(object):
    u'''
    式
    '''

    def __getattr__(self, attr):
        u'''
        属性アクセス
        '''
        
        return FuncCall(getattr, self, attr)
        
    

    def apply(self, *args, **argd):
        u'''
        関数呼び出し
        '''
        
        return FuncCall(self, *args, **argd)
        

    def __call__(self, *args, **argd):
        u'''
        関数呼び出しというか評価
        '''

        return self.eval(*args, **argd)


    def __getitem__(self, idx):
        u'''
        slice
        '''

        return Index(self, idx)


    @property
    def _m(self):

        return MethodGetter(self)



class MethodGetter(object):
    u'''
    メソッドを呼び出すために使う
    '''
    
    def __init__(self, obj):

        self.object = obj



    def __getattr__(self, attr):

        def call(*args, **argd):

            return FuncCall(getattr(self.object, attr), *args, **argd)

        return call



class FuncCall(Expression):
    u'''
    関数呼び出し
    '''

    def __init__(self, func, *args, **argd):

        self.function = to_expression(func)
        self.args = [to_expression(x)
                     for x in args]
        self.argd = dict((k, to_expression(v))
                          for k, v in argd.iteritems())


    def eval(self, *args, **argd):

        fargs = [x.eval(*args, **argd) for x in self.args]
        fargd = dict((k, v.eval(*args, **argd)) for k, v in self.argd.iteritems())

        return self.function.eval(*args, **argd)(*fargs, **fargd)



class List(Expression):

    def __init__(self, lst):

        self.items = map(to_expression, lst)
        

    def eval(self, *args, **argd):

        return [x.eval(*args, **argd) for x in self.items]



class Tuple(List):

    def eval(self, *args, **argd):

        return tuple(super(Tuple, self).eval(*args, **argd))




def __makeop():


    def make_operation(m):

        def operation(self, other):

            return FuncCall(m, self, other)

        return operation



    def make_roperation(m):

        def operation(self, other):

            return FuncCall(m, other, self)

        return operation


    def make_single(m):

        def operation(self):

            return FuncCall(m, self)
    

    compare = [
        'lt',
        'le',
        'eq',
        'ne',
        'gt',
        'ge',
        ]


    arismethic = [
        'add',
        'sub',
        'mul',
        'div',
        'floordiv',
        'mod',
        'pow',
        'lshift',
        'rshift',
        'and',
        'xor',
        'or',
        ]

    single = [
        'neg',
        'pos',
        'invert',
        'abs',
        ]

    for m in compare+arismethic:

        n = '__{0}__'.format(m)

        if not hasattr(operator, m):
            m += '_'

        setattr(Expression, n, make_operation(getattr(operator,m)))


    for m in compare+arismethic:

        n = '__r{0}__'.format(m)

        if not hasattr(operator, m):
            m += '_'

        setattr(Expression, n, make_roperation(getattr(operator,m)))


    for m in single:

        n = '__{0}__'.format(m)

        setattr(Expression, n, make_operation(getattr(operator,m)))


__makeop()




def slice_to_expression(sl):

    if isinstance(sl, slice):
        return slice(*[to_expression(x) for x in [sl.start, sl.stop, sl.step]])

    return to_expression(sl)



def eval_slice(sl, *args, **argd):

    if isinstance(sl, slice):
        return slice(*[x.eval(*args, **argd) for x in [sl.start, sl.stop, sl.step]])

    return sl.eval(*args, **argd)

    

class Index(Expression):
    u'''
    getitem した後
    '''

    def __init__(self, obj, idx):

        self.obj = to_expression(obj)

        self.index = slice_to_expression(idx)



    def eval(self, *args, **argd):

        return self.obj.eval(*args, **argd).__getitem__(eval_slice(self.index))




class Literal(Expression):
    u'''
    即値
    '''

    def __init__(self, value):

        self.value = value


    def eval(self, *args, **argd):

        return self.value


    def __call__(self, *args, **argd):
        u'''
        呼び出し可能オブジェクトのリテラルの場合だけ呼び出せる
        '''

        if hasattr(self.value, '__call__'):
            return self.apply(*args, **argd)
        else:
            return self.eval(*args, **argd)



class Placeholder(Expression):
    u'''
    引数のプレースホルダ
    '''

    def __init__(self, index):

        self.index = index



    def eval(self, *args, **argd):

        if isinstance(self.index, int):
            return args[self.index]

        elif isinstance(self.index, basestring):
            return argd[self.index]

        raise ValueError('invalid index type')
   


class PlaceholderMaker(object):


    def __getattribute__(self, key):

        return Placeholder(key)


    def __getitem__(self, key):

        return Placeholder(key)




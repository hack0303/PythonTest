# -*- coding: utf8 -*-
'''
Created on 2018��12��24��

@author: developorName
'''
from pip._vendor.six import assertCountEqual
'''
注意定义方法放的域
'''
def func01(x):
    print(list(range(x)))
#无值返回
def func02(param):
    for x in range(param):
        if x==param-1:
            print(x,end='\n')
        else:
            print(x,end=' ')
#有值返回
def func03(param):
    result=[]
    for x in range(param):
        result.append(x)
    return result
#
def ask_ok(prompt,retries=4,reminder="请重新尝试"):
    while True:
        ok=input(prompt)
        if ok in ['o','ok','okk']:
            return True
        if ok in ['f','fail','fai','faill']:
            return False
        retries=retries-1
        if retries<0:
            raise ValueError('超过用户响应次数')
        print(reminder)
i=5
def test(arg=i):
    print(arg)
sequence=[1,2]
def test002(arg=sequence):
    print(arg)
def test003(a,sequence=[]):
    sequence.append(a)
    print(sequence)
def test004(a,sequence=[]):
    if sequence is not None:
        sequence=[]
        sequence.append(a)
    print(sequence)
def test005(a,sequence=None):
    if sequence is None:
        sequence=[]
        sequence.append(a)
    print(sequence)
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
def testParam(param01,*param02,**param03):
    print(param01)
    for x in param02:
        print(x)
    for key in param03:
        print(key+":"+param03[key])
def concat(*args,seq='.'):
    print(seq.join(args))
def testabc(a,b='b',c='c',seq='.'):
    lst=[]
    lst.append(a)
    lst.append(b)
    lst.append(c)
    print(seq.join(lst))
def testabc_multiple(**args):
    for x in args:
        print("key:"+x+":"+args[x])
def testlambda(n):
    return lambda x:x+n
if __name__ == '__main__':
    func01(10)
    func02(10)
    print(func03(10))
    #----------以下是多参数定义-------------------
    ask_ok('请输入')
    ask_ok('请输入',2)
    #ask_ok('请输入','再来',2),错误，参数有序
    ask_ok('请输入',2,'再来')
    #测试引用外部变量(基本类型)作为默认值，结果表明，默认值为常量
    test()
    i=6
    test()
    #测试引用外部变量(对象)作为默认值,结果表明是对象内容可以改变
    test002()
    sequence.append(3)
    test002()
    #综上所述，引用指针不变，而对象内容可变
    #测试参数对象的共用现象
    test003(1)
    test003(2)
    test003(3)
    #不共用需要重新赋值新引用
    test004(1)
    test004(2)
    test004(3)
    #另一种写法，同上，这种会每次将参数置空
    test005(1)
    test005(2)
    test005(3)
    #总结同上，基本类型与对象引用里的区别
    #以下LINK：https://docs.python.org/3/tutorial/controlflow.html，都是直接复制黏贴
    parrot(1000)                                          # 1 positional argument
    parrot(voltage=1000)                                  # 1 keyword argument
    parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
    parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
    parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
    parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
    #parrot()                     # required argument missing
    #parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
    #parrot(110, voltage=220)     # duplicate value for the same argument
    #parrot(actor='John Cleese')  # unknown keyword argument
    '可变数量参数方法 Arbitrary Argument Lists'
    testParam('111')
    testParam('111','xxx','yyy',
              key='hehe',key02='haha')
    concat('a','b','c')
    concat('a','b','c',seq='x')
    #concat('a','b',seq='x','c')#error
    'Unpacking Argument Lists'
    print(list(range(3,6)))
    lst=[3,6]
    print(list(range(*lst)))
    #测试可见，拆包用的序列中的前两个值
    lst=[3,4,6]
    print(list(range(*lst)))
    #注意解包符号
    testabc(**{'a':'a','b':'b','c':'c'})
    testabc_multiple(**{'a':'a','b':'b','c':'c','d':'d'})
    #测试返回值为lambda
    f=testlambda(100)
    print(f(1))
    #测试参数为lambda,按照元组中第二个值作为Key
    pairs=[(1,'one'),(2,'two'),(3,'three'),(4,'four')]
    pairs.sort(key=lambda pair:pair[1])
    print(pairs)
    pass
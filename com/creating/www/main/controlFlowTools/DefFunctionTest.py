# -*- coding: utf8 -*-
'''
Created on 2018��12��24��

@author: developorName
'''
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
    pass
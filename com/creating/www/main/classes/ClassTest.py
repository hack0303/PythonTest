# -*- coding: utf8 -*-
'''
Created on 2018��12��26��

@author: developorName
'''
'''

'''
def scope_test():
    def do_local():
        test='local'#do_local方法内分配
        pass
    def do_nonlocal():
        nonlocal test#外部方法分配
        test='nonlocal'
        pass
    def do_global():
        global test
        test='global'#模块级别分配，即外部方法外
        pass
    test='test'
    do_local()
    print(test)
    do_nonlocal()
    print(test)
    do_global()
    print(test)
#<<总结,实际上虽名称一样，使用的并不是同一个分配的地方的数据 
class T:
    def __init__(self):
        self.name='he'
class T_:
    name='ni'
    def __init__(self):
        self.name='haha'
        
    #def __init__(self,a,b):#好像只能有一个构造器
    #    self.a=a
    #    self.b=b
    def operate(self):
        print('operate001')
       
class A():
    a='a'
class B():
    b='b'
class C():
    c='c'
class A2(A):
    a2='a2'
class Multiple(A,B,C):
    m='multiple'
if __name__ == '__main__':
    scope_test()
    print(test)
    t1=T()
    t2=T_()
    print(t1.name,t2.name)
    t2.operate()
    t3=A2()
    print(t3.a)
    t4=Multiple()
    print(t4.m,t4.a,t4.b,t4.c)
    print('-'*40)
    print('以上都为多重继承和public的展示')
    class P():
        __p='private'
        def printx(self):
            print(self.__p)
    p=P()
    #print(p.p)
    p.printx()
    #Odds and Ends
    class Animal():
        pass
    animal=Animal()
    animal.name='小黑'
    animal.type='dog'
    animal.age=5
    print(animal.name,animal.type,animal.age)
    pass
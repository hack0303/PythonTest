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
if __name__ == '__main__':
    func01(10)
    func02(10)
    print(func03(10))
    pass
# -*- coding: utf8 -*-
'''
Created on 2018年12月25日

@author: developorName
'''

if __name__ == '__main__':
    year=2018
    month=12
    day=25
    print(f'{year}年{month}月{day}日')
    yes_vote=10_100_100
    no_vote=10_100_100
    percentage=yes_vote/(yes_vote+no_vote)
    print('{:-9} yes vote ,{:2.2%}'.format(*[yes_vote,percentage]))
    #debug or test can use repr() str(),most case,they is same,under is distinguish them
    #repr() 意思 representation
    print(str('hello,world'))
    print(repr('hello,world'))
    print(str('hehe\n'))
    print(repr('hehe\n'))
    print(str([1,(1,2)]))
    print(repr([1,(1,2)]))# The argument to repr() may be any Python object:
    #总结，repr()更表达原始数据的真实结果，包括它的形式。而str（）就是旨在人类可读
    import math
    print(f'圆周率:{math.pi:.3f}')
    v='大家好'
    print(f'强制{v!a}')#equal to ascii()
    print(f'强制{v!s}')#equal to str()
    print(f'强制{v!r}')#euqal to repr()
    dct=dict([('哈哈',1),('呵呵',1),('嘻嘻',1)])
    for x,y in dct.items():
        print(f'{x:9} ==> {y:9}')#注意不同类型的不同格式化参数，不是互相兼容
    #format()
    print('{0},{1},{2}'.format(*[1,2,3]))
    print('{0},{1},{key}'.format(1,2,key='3'))
    print('{1},{0}'.format(1,2))
    print('{key1},{key2}'.format(key1=1,key2=2))
    dsc={'a':1,'b':2,'c':3}
    print('a:{0[a]:d},b:{0[b]:d},c:{0[c]:d}'.format(dsc))#0表示的是元组中的元素索引，语义应该是比较对应索引和指定key值，相等拿出对应值
    #print('a:{1[1]:s},b:{1[2]:s},c:{1[3]:s}'.format(dsc)),好像只能用于这种字典
    print('{a:d},{b:d},{c:d}'.format(**dsc))
    for x in range(1,11):
        print('{0:d} {1:d} {2:d}'.format(x,x*x,x*x*x))
    for x in range(1,11):
        print('{0:2d} {1:3d} {2:5d}'.format(x,x*x,x*x*x))#有位置时可以右对齐，没有的时候左对齐依次朝后
    #Manual String Formatting
    for x in range(1,11):
        print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
        print(repr(x*x*x).rjust(5))
    print('12'.zfill(5))
    print('-12'.zfill(5))
    print('-1.23'.zfill(5))
    print('1.13141515'.zfill(7))
    #以上0扩展，算符号，算小数点进符号位
    #import math
    print('pi: %5.3f' % math.pi )#老版的字符串format
    pass
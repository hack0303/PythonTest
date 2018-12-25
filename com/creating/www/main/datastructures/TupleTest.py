# -*- coding: utf8 -*-
'''
Created on 2018��12��25��

@author: developorName
'''
'''
需要注意的单元素元组的创建与赋值
其中，创建时不管加不加括号，单元素时都需要右侧逗号，
在拆解赋值成单元素变量时，元素只有一个时，左侧需要加入逗号
都是一些解析上的规则，注意就行
'''
if __name__ == '__main__':
    tpl=1,2
    print(tpl)
    tpl=1,#注意后面的逗号，与正常的其他基本类型和对象区分
    print(tpl)
    print(len(tpl))
    tpl=tpl,3
    print(tpl)
    tpl=(1,)
    #tpl=(1)
    print(tpl)
    #<<总结以上，单元素需要加入逗号区分与一般非聚合元素之间的区别
    #tpl[0]=1#TypeError: 'tuple' object does not support item assignment
    empty=()
    print(len(empty))
    tpl=(1,)
    x,=tpl
    #x=tpl#不加逗号就变成复制元组了,注意左右的逗号
    print(x)
    tpl=1,2,3
    x,y,z=tpl
    print(x,y,z)
    pass
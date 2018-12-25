# -*- coding: utf8 -*-
'''
Created on 2018��12��25��

@author: developorName
'''

if __name__ == '__main__':
    #字典遍历
    name2age_dict={'pig':1,'dog':2,'cat':3}
    print([(x,y) for x,y in name2age_dict.items()])
    #列表遍历
    lst=['a','b','c']
    for index,value in enumerate(lst):
        print(index,value)
    A_lst=['name','age','tel']
    B_lst=['xx',111,10086]
    #组合格式化
    for x,y in zip(A_lst,B_lst):
        print("quest {0}?answer {1}".format(x,y))
    #数值反转
    for x in reversed(range(1,30,3)):
        print(x)
    #非NAN的值
    import math
    raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
    result=[]
    for value in raw_data:
        if not math.isnan(value):
            result.append(value)
    print(result)
            
    pass
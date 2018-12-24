# -*- coding: utf8 -*-
'''
Created on 2018��12��24��

@author: developorName
'''

if __name__ == '__main__':
    while(True):
        x=int(input("请输入数值:"))
        if x<10:
            print("小于10的值")
        if x==10:
            print("等于10的值")
        if x>=1000 and x>=0:
            print("大于10的值")
        elif x<0:
            print("小于0的值")
        else:
            print(">10,<1000的值")
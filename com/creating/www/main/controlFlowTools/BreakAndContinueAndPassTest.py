# -*- coding: utf8 -*-
'''
Created on 2018��12��24��

@author: developorName
'''

if __name__ == '__main__':
    for x in range(5):
        print(x)
        if x==2:
            break
    print("--------------------")
    for x in range(10):
        if x>2 and x<7:
            print(x)
            continue
    print("--------------------")
    #pass相等于nop，在python中表示什么都不做，目前看来，只是因为python这种对齐结构而出的结构对齐
    for x in range(10):
        if x<=2:
            pass
        elif x>=7:
            pass
        else:
            print(x)       
    pass
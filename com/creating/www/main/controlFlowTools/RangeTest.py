# -*- coding: utf8 -*-
'''
Created on 2018��12��24��

@author: developorName
'''

if __name__ == '__main__':
    #默认
    for x in range(5):
        print(x)
    #start,end，step
    for x in range(5,10,1):
        print(x)
    for x in range(10,100,10):
        print(x)
    for x in range(-10,-100,-30):
        print(x)
    #iterate sequence througth index
    words=["dog","pig","cat"]
    for x in range(len(words)):
        print((x,words[x]))
    #print test
    print(range(5))
    print(list(range(5)))
    pass
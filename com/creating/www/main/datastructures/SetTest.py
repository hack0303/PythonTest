# -*- coding: utf8 -*-
'''
Created on 2018��12��25��

@author: developorName
'''

if __name__ == '__main__':
    animals={'pig','dog','cat'}
    print('pig' in animals)
    print('bird' in animals)
    animal_letters={'pig'}
    #以下两种都可以判断是否在字符串中，但他们集合对象不同，用的方法实际上不同的，在下述集合的操作中，就可以发现，字符串是没有交叉并这些方法的
    print('p' in animal_letters)
    animal_letters='pig'
    print('p' in animal_letters)
    animal_letters=set('pig')
    print('i' in animal_letters)
    A=set('abc')
    B=set('cde')
    print(A-B)#差,1
    print(A|B)#并,2
    print(A&B)#交,3
    print(A^B)#并中去了交,4,(2-3)
    #<<实际上仔细观察，实际上他们的结果都是用的新集合，即结果不影响原始集合，实际上JAVA中就不是这样，原始集合会受到影响，当然拷贝出来就不会影响。
    #一个集合遍历，语法糖
    print([x for x in 'abcde' if x not in 'bcd'])
    pass
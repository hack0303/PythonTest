# -*- coding: utf8 -*-
'''
Created on 2018��12��25��

@author: developorName
'''

if __name__ == '__main__':
    name2age={'a':11,'b':14,'c':13}
    name2age_=dict([('a',11),('b',14),('c',13)])#->dictionary,方法1,list+tuple
    print(name2age)
    print(name2age_)
    print([str(x) for x in name2age])
    #print([str(x)==str(y) for x in name2age for y in name2age_])#写的不对，想比较key,以后改
    del name2age['a']
    print(name2age)
    name2age.setdefault('a', 11)
    print(name2age)
    print(list(name2age))
    print(sorted(name2age))
    print(name2age)
    print('a' in name2age)
    print({x:x**2 for x in range(10)})#->dictionary,方法2
    #方法3的限制，key只能是简单字符串
    print(dict(x=1,y=4,z=9))#->dictionary,方法3,When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
    pass
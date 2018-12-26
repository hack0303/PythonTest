# -*- coding: utf8 -*-
'''
Created on 2018��12��26��

@author: developorName
'''
class Reverse():
    def __init__(self,data):
        self.data=data
        self.index=len(data)-1
    def __next__(self):#重要
        if self.index < 0:
            raise StopIteration
        else:
            index=self.index
            self.index=self.index-1
            return self.data[index]
    def __iter__(self):#重要
        return self
if __name__ == '__main__':
    for element in [1, 2, 3]:#列表
        print(element)
    for element in (1, 2, 3):#元组
        print(element)
    for key in {'one':1, 'two':2}:#字典
        print(key)
    for char in "123":#字符串中的字列表
        print(char)
    for line in open("test.txt"):#文件数据中的行记录
        print(line, end='')
    test='abcd'
    it=iter(test)
    for x in range(len(test)):
        print(next(it))
    reverse=Reverse('abcde')
    it=iter(reverse)
    for x in reverse:
        print(x)
    print('-'*40)
    #Generators
    def reverse(data):
        for x in range(len(data)-1,-1,-1):
            yield data[x]#Anything that can be done with generators can also be done with class-based iterators as described in the previous section. What makes generators so compact is that the __iter__() and __next__() methods are created automatically.
    print([x for x in reverse('abcde')])
    #Generator Expressions>>
    print(sum([x for x in range(5)]))
    lst_x=[x for x in range(1,5,1)]
    lst_y=[x for x in range(5,9,1)]
    print([x*y for x,y in zip(lst_x,lst_y)])
    pass
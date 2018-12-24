# -*- coding: utf8 -*-
'''
Created on 2018��12��24��

@author: developorName
'''

if __name__ == '__main__':
    words=["dog","pig","bird"]
    for word in words:
        print(word)
    '''
        遍历时需要浅拷贝集合
    '''
    '''
    for word in words[:]:
        if word==words[0]:
            words.remove(word)
    '''
    x=0
    for word in words[:]:
        if word==words[x]:
            words.insert(words.__len__(),word)   
        x=x+1
    for word in words:
        print(word)
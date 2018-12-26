# -*- coding: utf8 -*-
'''
Created on 2018��12��26��

@author: developorName
'''
class UserException(Exception):
    pass
'''
class UserError(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
'''
if __name__ == '__main__':
    x=1
    try:
        raise Exception()
    except Exception as e:
        x=x**2
        print('catch exception',x)
    finally:
        x=x+1
        print('do finally thing',x)
    try:
        x=1
    except Exception as e:
        x=x**2
        print('catch exception',x)
    finally:
        x=x+1
        print('do finally thing',x)
    with open("test.txt") as f:#Predefined Clean-up Actions
        for line in f:
            print(line, end="")
    #https://docs.python.org/3/tutorial/errors.html
    #和其他语言基本一样，请参考JAVA 
    pass
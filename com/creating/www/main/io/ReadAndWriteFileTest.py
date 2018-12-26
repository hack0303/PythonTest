# -*- coding: utf8 -*-
'''
Created on 2018年12月25日

@author: developorName
'''
import os
if __name__ == '__main__':
    #print(os.getcwd())
    with open('resources/test.txt') as f:#只能读取模块路径下文件，读取其他文件除了全路径外，可能需要修改一些默认路径参数,待解决
        read_data=f.read()
        print(read_data)
    f.close()
    print('-'*40)
    with open('resources/test.txt') as f:
        print(repr(f.readline()))
        print(repr(f.readline()))
        print(repr(f.readline()))
        print(repr(f.readline()))
        print(repr(f.readline()))
    f.close()
    print('-'*40)
    with open('resources/test.txt') as f:
        print(f.readline(),end=' ')
        print(f.readline(),end=' ')
        print(f.readline(),end=' ')
        print(f.readline(),end=' ')
        print(f.readline(),end=' ')
    f.close()
    print()
    print('-'*40)
    with open('resources/test.txt') as f:
        line=f.readline()
        while line != '':
            print(line,end='')
            line=f.readline()
    f.close()
    print()
    print('-'*40)
    with open('resources/write.txt','w') as f:
        f.write('haha\n')
        f.write('haha\n')
        f.write('haha\n')
    f.close()
    print()
    print('-'*40)
    with open('resources/test.txt') as f:
        line=f.readline()
        print(f.tell())
        print(line,end=' ')
        print(f.seek(0))
        line=f.readline()
        print(line,end=' ')
        print(f.seek(3))
        line=f.readline()
        print(line,end=' ')
        #print(f.seek(100))
        #print(f.seek(4097))
        print(f.seek(3,0))
        line=f.readline()
        print(line,end=' ')
        print(f.tell())
    f.close()
    import json
    print(json.dumps([1,'哈哈','e']))#查看dump后的结果形式
    with open('resources/dump.txt','w') as f:#序列化
        json.dump([1,'hehe','嘿嘿'],f)
    f.close()
    x=None
    with open('resources/dump.txt') as f:#反序列化 
        x=json.load(f)
    f.close()
    print(x)
    pass
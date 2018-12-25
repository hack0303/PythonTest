# -*- coding: utf8 -*-
'''
Created on 2018年12月25日

@author: developorName
'''
'''
Link:https://docs.python.org/3/tutorial/datastructures.html
The list data type has some more methods. Here are all of the methods of list objects:

list.append(x)
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.clear()
Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])
Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)
Return the number of times x appears in the list.

list.sort(key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Equivalent to a[:].
'''
if __name__ == '__main__':
    lst=['a','b','c','d','e','a']
    print('计算指定值重复次数:',lst.count('a'))
    lst.append('f')
    print('末尾追加:',str(lst))
    lst.insert(0,'g')
    print('索引处开始序列后移:',str(lst))
    lst.remove('g')
    print('删除指定值:',str(lst))
    lst.pop(0)
    print('弹出指定指定索引位置值:',str(lst))
    lst.pop()
    print('不指定值，弹出position序下最后索引位置值:',str(lst))
    #搜索指定区间内的是否有指定值，返回对应的索引，如果没有，报错
    print(lst.index('b'))
    print(str(lst))
    #lst.index('b',start=2)
    #print(str(lst))
    #lst.index('c',end=1)
    #print(str(lst))
    print(lst.index('c',1,3))
    print(str(lst))
    #反转
    lst.reverse()
    print(lst)
    #appendAll 相当于a[len(a):]=['a','a','a']
    lst.extend(['a','a','a'])
    print(lst)
    #浅拷贝，正向排序，反向排序，清空序列，排序还可以指定Key
    lst2=lst.copy()
    lst.sort()
    print(lst)
    lst.sort(reverse=True)
    print(lst)
    lst.clear()
    print(str(lst),str(lst2))
    print('-'*40)
    print('作为栈使用:')
    stack=['a','b','c','d']
    print(str(stack))
    stack.append('e')
    print("进栈:",stack)
    stack.pop()
    print("出栈:",stack)
    print('-'*40)
    print('作为队列使用:')
    from collections import deque
    queue=deque(['a','b','c','d'])
    print(str(queue))
    queue.append('e')
    print(str(queue))
    queue.popleft()
    print(str(queue))
    #以下都是一些list的语法糖
    squares=[]
    squares=list(map(lambda x:x**2,range(10)))
    print(squares)
    squares=[x**2for x in range(10)]
    print(squares)
    squares=[(x,y) for x in range(10) for y in range(10) if x !=y]
    print(squares)
    matrix=[[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12]]
    print(matrix)
    #打印col
    print([[row[i] for row in matrix] for i in range(4)])
    cols=[[row[i] for row in matrix] for i in range(4)]
    'In the real world, you should prefer built-in functions to complex flow statements. The zip() function would do a great job for this use case:'
    #看似只是把可变变成不可变的元组，不知道是不是起到压缩空间的作用，待议
    print(list(zip(*cols)))
    #del
    test=[x for x in range(10)]
    del test[1:2]
    print("给定开始结束:",test)
    del test[:1]
    print("给定结束索引:",test)
    del test[3:]
    print("给定开始索引:",test)
    del test[:]
    print("删除全部",test)
    test_ref=test
    del test
    print("删除整个变量")
    #test
    #test不可以再被引用,因为没有定义，实际不知道是不是释放了与之相关的全部资源，比如内存 
    #测试说明，只是删除这个这个引用变量，并不会进行立刻的内存释放，如果参照JAVA，全部都没有引用时，会自动对引用的内容进行内存释放
    print(test_ref)
    pass
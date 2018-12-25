# -*- coding: utf8 -*-
'''
Created on 2018��12��25��

@author: developorName
'''
'''
Sequence objects may be compared to other objects with the same sequence type. The comparison uses lexicographical ordering: first the first two items are compared, and if they differ this determines the outcome of the comparison; if they are equal, the next two items are compared, and so on, until either sequence is exhausted. If two items to be compared are themselves sequences of the same type, the lexicographical comparison is carried out recursively. If all items of two sequences compare equal, the sequences are considered equal. If one sequence is an initial sub-sequence of the other, the shorter sequence is the smaller (lesser) one. Lexicographical ordering for strings uses the Unicode code point number to order individual characters. Some examples of comparisons between sequences of the same type:
'''
'''
翻译:
可以将序列对象与具有相同序列类型的其他对象进行比较。比较使用词典排序：首先比较前两个项目，如果它们不同，则确定比较的结果;如果它们相等，则比较接下来的两个项目，依此类推，直到任一序列用完为止。
如果要比较的两个项本身是相同类型的序列，则递归地执行字典比较。如果两个序列的所有项目相等，则认为序列相等。如果一个序列是另一个序列的初始子序列，则较短的序列是较小的（较小的）序列。
字符串的字典顺序使用Unicode代码点编号来排序单个字符。相同类型序列之间比较的一些示例：
'''
if __name__ == '__main__':
    print((1,2,3)<(1,2,4))
    print([1, 2, 3]<[1, 2, 4])
    print('ABC' < 'C' < 'Pascal' < 'Python')
    print((1, 2, 3, 4)< (1, 2, 4))
    print((1, 2) < (1, 2, -1))
    print((1, 2, 3) == (1.0, 2.0, 3.0))
    print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))
    #print((1,2,(3,4))>(1,2,3))#序列元素对应元素类型必须一样
    print((1,2,(3,4))>(1,2))#这个可以运行，由此证明runtime check
    pass
#!/usr/bin/python3
#coding:utf-8

import os

# os.path.dirname(__file__)的作用是 返回脚本的路径，即文件路径中所在的目录（不包含文件名）
# path = os.path.dirname(r'C:\softwares\python3.6.5\2020test\p1.py')
# print (path)

# path = os.path.dirname(r'\p1.py')  # 返回为空
# print(path)


# os.path.abspath(__file__)返回的是.py文件的绝对路径,__file__为内置属性
def getCurPath1():
    cur_path = os.path.dirname(os.path.realpath(__file__))
    return cur_path

def getCurPath2():
    cur_path = os.getcwd()
    return cur_path

print('func1---'+ getCurPath1())
print('func2--'+ getCurPath2())

'''
这里的func1就是os.path.dirname(os.path.realname(file))获取的__file__所在脚本的路径，也就是getRootPath.py的路径。
而os.getcwd()获取的当前最外层调用的脚本路径，即getPath所在的目录也可描述为起始的执行目录，A调用B，起始的是A，那么获取的就是A所在的目录路径。

'''

'''
不同点
example:
file_a
file_b -> file_a # 软连接指向a

>>> import os

>>> os.path.abspath(file_b)
/tmp/file_b

# 会得到指向的文件的路径
>>> os.path.realpath(file_b)
/tmp/file_a

'''
# -*- coding: UTF-8 -*-

'''
file.read([size])
从文件读取指定的字节数，如果未给定或为负则读取所有。
'''
with open('123.txt','r') as file:
	count = 0
	content = file.read()
	for i in content:
		if i.isupper():
			count += 1

print(count)

#输入任意字符串，统计大小写字母和数字的个数
def count_char(s):
	if len(s) == 0:
		return 0,0,0
	Capital_num, Lower_num, number_num = 0,0,0
	for char in s:
		if char.isupper():
			Capital_num += 1
		elif char.islower():
			Lower_num += 1
		elif char.isdigit():
			number_num += 1
	return Capital_num,Lower_num,number_num

s = " Hello Csdn 999m Hello PYthon"
x1 ,x2,x3 = count_char(s)
print(f"大写字母共有{x1}个，小写字母共有{x2}个,数字共有{x3}个")

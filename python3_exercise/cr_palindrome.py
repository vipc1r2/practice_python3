# -*- coding: UTF-8 -*-

# python自带翻转函数reversed()实现回文字符串算法
# def is_plalindrome(string):
#     return string == ''.join(list(reversed(string)))
#
# print(is_plalindrome('123 321'))
# print(is_plalindrome('taco cat'))

# 检查给定的字符串是不是回文序列，它首先会把所有字母转化为小写，并移除非英文字母符号。最后，它会对比字符串与反向字符串是否相等，相等则表示为回文序列。
# def palindrome(string):
#     from re import sub
#     s = sub('[\W_]', '', string.lower())  # 首先会把所有字母转化为小写，并移除非英文字母符号
#     return s == s[::-1]
#
# print(palindrome('taco cat'))


def palindrome1():
	a=input("enter sequence")
	b=a[::-1]
	if a==b:
		print("palindrome")
	else:
		print("Not a Palindrome")

palindrome1()
# -*- coding: UTF-8 -*-

Number = int(input("请输入一个数字： ")) # 输入一个正整数，并赋值给Number

if Number > 1:                          # 判断输入的正整数是否大于1
    for i in range(2,Number):           # 循环取出2至Number-1的正整数 i
        if Number % i == 0:             # 将Number与i取余，如果余数为0 ，则就可以被整除
            print("数字%s不是素数" % Number)
            break                       # 不是素数，结束循环
    else:
        print("数字%s是素数" % Number)  # 否则就是素数，打印结果

else:
    print("输入的数字小于1，这是不合法的。")
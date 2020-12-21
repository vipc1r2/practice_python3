# 实现fibonacci数列的三种方法,斐波那契数列（Fibonacci sequence），又称黄金分割数列

# 递归法
def fibo(n):
    if n < 3 :
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(6))
# 费波那契系数是：0,1,1,2,3,5,8,13,21,34,55,89,144,233……


# 循环
def fibo1(n):
    a, b = 1,1
    for i in range(n):
        a,b = b,a+b
    return a

print(fibo1(6))


# 生成器
def fibo2(n):
    a, b = 1, 1
    while n:
        yield a
        a, b = b, a+b
        n -= 1
print(type(fibo2(6)))

# for i in fibo2(6):
#     print(i)



def fibo3(n):
    a,b=0,1
    while n<100:
       print(b)
       a,b=b,a+b

print(fibo(10))

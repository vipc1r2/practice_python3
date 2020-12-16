def rpad(src,length,string):
    while len(src) < length:
        for i in string:
            src += i
            if len(src) >= length:
                return "" + src
    else:
        return "" + src

print(rpad("abcd", 10, "12"))   # 10位
print(rpad("bbbb", 11, "12"))   # 11位
print(rpad("cccc", 12, "12"))   # 12位
print(rpad("dddd", 13, "0"))   # 13位
print(rpad("ffff", 13, " "))   # 13位有空格
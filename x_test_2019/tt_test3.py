# for循环方法实现星星三角
def triangle():
    for i in range(0,5):
        for j in range(i+1):
            if i == 4:
                print('* ',end="")
                continue
            if j == 0 or j == i:
                print("* ",end = "")
            else:
                print(" ",end="")
        print()

    print("+"*11)
    # 实心三角
    for i in range(5):
        print("* "* (i+1))

    # 实心正方形
    print("+" * 11)
    for i in range(5):
        print("* "*5)

    # 空心正方形
    print("+" * 11 + "空心正方形")
    for i in range(4):
        if i == 0:
            print("* " * 5)
        if i == 3:
            print("* " * 5)
            continue
        for j in range(5):
            if j == 0:
                print("* ", end=" ")
            if j == 4:
                print("* ")
            else:
                print(" ", end="")

    # 金字塔
    print("+" * 11 + "金字塔")
    for i in range(5):
        print(" " * (4 - i), end="")
        print("* " * (i + 1))




if __name__ == '__main__':
    triangle()


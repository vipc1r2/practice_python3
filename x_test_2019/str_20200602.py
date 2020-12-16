def no_repeat_str(s):
    '''找出来一个字符串中最长不重复子串'''
    res_list = []  # 建立空列表，留作容器，放字符串的不重复的元素用
    length = len(s) # 字符串长度
    for i in range(length):  # 依次把0、1、2、len(s)长度-1给i
        tmp = s[i] # 字符串下角标s[0]对应字符串中第一个元素
        for j in range(i + 1, length):  # 遍历，不存在则拼接，已存在则打断循环
            if s[j] not in tmp:
                tmp += s[j]  # s[i]+s[j]拼接到一起存入tmp
            else:
                break
        res_list.append(tmp)  # 构造子串列表
    # 以下代码目的是取子串列表中长度最大的元素,方法很多，以下是两种思路：
    # 方法一（冒泡排序）：
    for i in range(len(res_list) - 1): # 利用len得到列表长度，长度-1就是遍历次数[1,22,345,6]
        for j in range(len(res_list) - i - 1):

            if len(res_list[j]) > len(res_list[j+1]): # 比较相邻的列表元素
                res_list[j], res_list[j+1] = res_list[j+1], res_list[j]  # 从小往大排序显示
    """
    # 方法二（选择排序）：
    for i in range(len(res_list)):  
        k = i
        j = i + 1j
        while j < len(res_list):
            if len(res_list[k]) > len(res_list[j]):
                k = j
            j += 1
        if i != k:
            res_list[i], res_list[k] = res_list[k], res_list[i]
        """

    return res_list[-1]  # 取列表最后一个元素


if __name__ == '__main__':
    str_list = ['aabcdaeeaabc', 'fdsaefkjkgdok', 'jhrd123xfdsa8042d5439']  # 这是一个列表
    for s in str_list:  # 遍历列表元素，赋值给s
        res = no_repeat_str(s)  # 把s调用函数str_repeat_str
        print('%s最长非重复子串为：%s,长度为: %s' % (s, res, len(res)))
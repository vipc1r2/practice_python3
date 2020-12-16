#
# import os
# import chardet
#
# def get_encoding(filename):
#     try:
#         f = open(filename,"rb")
#         data = f.readline()
#         f.close()
#         encoding = chardet.detect(data)
#         print(encoding)
#         return encoding['encoding']
#     except Exception as e:
#         print("获取文件编码出错")
#
# def count_word(filename):
#     if not os.path.exists(filename):
#         print("文件不存在")
#         return None
#     dic_c = {}
#     try:
#         encoding_ = get_encoding(filename)
#         with open(filename,'rb') as f:
#             for line in f:
#                 strings = line.split()
#                 for word in strings:
#                     word = word.lower()
#                     if word not in dic_c.keys():
#                         dic_c[word]=1
#                     else:
#                         dic_c[word] += 1
#         # print(dic_c)
#         sort_dic_c = sorted(dic_c.items(),key=lambda item: item[1],reverse=True)
#         # print(sort_dic_c)
#         word_count = []
#         for i in sort_dic_c:
#             word = i[0].decode(encoding_)
#             # print(word)
#             count = i[1]
#             # print(count)
#             word_count.append('word'+'count')
#
#         return word_count
#         print(word_count)
#
#     except Exception as e:
#         print("出现异常： ",e)
#         return None

"""
#统计1000w行的文件中，字符串出现的次数并排序，其中字符串以空格分割
#我认为需要考虑三个问题
1、大文件的读取，一行一行读入，避免一次性读入，内存溢出的情况
2、文件编码格式的处理，避免乱码
3、python中字典对象的排序，按value值排序
"""
import os
import chardet
def get_encoding(filename):
    """
    :param filename: 文件路径
    :return:  文件编码类型
    """
    try:
        f = open(filename,"rb")
        data = f.readline()
        f.close()
        encoding = chardet.detect(data)
        print(encoding)
        return encoding['encoding']
    except Exception as e:
        print("获取文件编码出错")

def count_word(filename):
    """
    :param filename: 文件路径
    :return: None 操作异常；
            ss 列表，列表中的每一个元素为包含两个元素的元组，
            元组的第一个元素为文中出现的字符串，第二个元素为其在文中出现的次数，按出现次数升序排序
    """
    if not os.path.exists(filename): #检查文件是否存在
        print("文件不存在")
        return None
    dic_c = {} #用字典来存储每个字符串出现的次数，key为字符串，value 为次数
    try:
        encoding_ = get_encoding(filename)  #获取文件编码方式，避免出现乱码
        with open(filename, "rb")as f:  # 以rb形式读入，速度会快
            for line in f: #一行一行读入，避免内存溢出的情况
                strings = line.split()  # 分割一行,以空格分隔
                for word in strings:
                    word = word.lower()  #全部转化为小写
                    if word not in dic_c.keys():  # 第一次出现
                        dic_c[word] = 1
                    else:
                        dic_c[word] += 1  # 出现次数加1

        sort_dic_c = sorted(dic_c.items(), key=lambda item: item[1],reverse=True)  # 按出现次数排序，升序 如果需要逆序的话，reverse=True即可
        word_count = []
        for i in sort_dic_c:
            word = i[0].decode(encoding_)  #对二进制串进行解码
            count = i[1]
            word_count.append((word,count))
            # word_count.append(word)
            # print(word_count)
        # return  word_count
        print(word_count)
    except Exception as e: #出现异常，打印异常 ，返回None
        print("出现异常：",e)
        return None






if __name__ == '__main__':
    filename = r"C:\Users\xudongliang\Desktop\2020_08_26\1.txt"
    # res=get_encoding(filename)

    count1= count_word(filename)

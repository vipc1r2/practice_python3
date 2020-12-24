# -*- coding: UTF-8 -*-

# 快速排序
def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left,(int, float)) else left # isinstance判断一个对象是否是一个已知的类型（int、float），是这个元组里的类型就返回true
    right = len(arr)-1 if not isinstance(right,(int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr

def partition(arr, left, right): # 是角标
    pivot = left
    index = pivot+1
    i = index
    while  i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index+=1
        i+=1
    swap(arr,pivot,index-1)
    return index-1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

if __name__ == '__main__':
    list = [6,1,2,7,9,3,4,5,10,8]
    print("List source is:", list)
    result = quickSort(list)
    print("List sort is:", result)


'''
①从数列中挑出一个元素，称为 “基准”（pivot）；
②重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
'''
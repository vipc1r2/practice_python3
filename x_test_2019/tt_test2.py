# 用python冒泡排序
# 从左向右，两两比较
def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]  # 交互他们的值
    return nums


if __name__ == '__main__':
    nums = [ 83, 16, 9, 96, 27, 75, 42, 69, 34]
    bubble_sort(nums)
    print(nums)


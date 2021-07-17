# encoding = utf-8
# def mergeSort(alist):
#     if len(alist) <= 1:
#         return alist
#     # 二分分解
#     num = len(alist) // 2
#     left = mergeSort(alist[:num])
#     print(alist)
#     right = mergeSort(alist[num:])
#     # 合并
#     return merge(left,right)
#
# def merge(left, right):
#     '''合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组'''
#     #left与right的下标指针
#     l, r = 0, 0
#     print("left",left)
#     print("right",right)
#     result = []
#     while l<len(left) and r<len(right):
#         if left[l] < right[r]:
#             result.append(left[l])
#             l += 1
#         else:
#             result.append(right[r])
#             r += 1
#     # 这里是因为左右两个列表的长度可能不一致，因此可能会出现其中一个列表并没有指向最后的索引
#     # 但是这里不知道是左右列表中的那哪一个，因此，要对左右列表剩下的值进行合并
#     result += left[l:]
#     result += right[r:]
#     print("result", result)
#     return result
#
# alist = [54,26,93,17,77,31,44,55,20]
# sorted_alist = mergeSort(alist)
# print(sorted_alist)


def mergeSort(alist):
    # 注意这里的结束条件，是<=1，因为如果长度为1的话，就达到我们分隔的目的，就可以返回
    # 这个与二分查找的结束循环条件不一致
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    left = mergeSort(alist[:mid])
    right = mergeSort(alist[mid:])
    return merge(left,right)


def merge(left,right):
    l,r = 0,0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    # 这里边的left和right其实本质上是已经拍好顺序的
    result = result + left[l:]
    result = result + right[r:]
    print(result)
    # while l < len(left) or r < len(right):
    #     if l < len(left) and r < len(right):
    #         if left[l] < right[r]:
    #             result.append(left[l])
    #             l += 1
    #         else:
    #             result.append(right[r])
    #             r += 1
    #     elif l < len(left):
    #         result.append(left[l])
    #         l += 1
    #     else:
    #         result.append(right[r])
    #         r += 1
    return result

alist = [54,26,93,17,77,31,44,44,55,20]
sorted_alist = mergeSort(alist)
print(sorted_alist)


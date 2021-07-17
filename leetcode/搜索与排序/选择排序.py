# encoding = utf-8
def bubble_sort(alist):
    #第一层循环控制对比的次数 比如 一共有8个数字，第一次要对比7次
    n = len(alist)
    for i in range(n-1):
        min_index = i
        for j in range(i,n):
            if alist[j] < alist[min_index]:
                min_index = j
        if min_index != i:
            alist[min_index],alist[i] = alist[i],alist[min_index]

    return alist
li = [54,26,93,17,77,31,44,55,20]
print(bubble_sort(li))

# 最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束。）
# 最坏时间复杂度：O(n2)
# 稳定性：稳定
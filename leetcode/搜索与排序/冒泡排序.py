# encoding = utf-8
def bubble_sort(alist):
    #第一层循环控制对比的次数 比如 一共有8个数字，第一次要对比7次
    n = len(alist)
    for i in range(n-1):
        # 每次最大值会被移动到右端，因此这里下一次循环的时候是j取值是到n-1-i
        for j in range(n-1-i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
        print(alist)
    return alist
li = [54,26,93,17,77,31,44,55,20]
print(bubble_sort(li))

# 最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束。）
# 最坏时间复杂度：O(n2)
# 稳定性：稳定
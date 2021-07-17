def quickSort(start,end,alist):
    if start >= end:
        return
    i = start
    j = end
    mid = alist[start]
    while i < j:
        while i < j and alist[j] >= mid:
            j -= 1
        alist[i] = alist[j]
        while i<j and alist[i] < mid:
            i += 1
        alist[j] = alist[i]
    alist[j] = mid
    quickSort(start,i-1,alist)
    quickSort(i+1,end,alist)

a = [54,26,93,17,77,17,31,44,55,20]
quickSort(0,len(a) - 1,a)
print(a)



# 归并排序分两步，第一步是将其分开，第二步是将其组合
def spiltSort(alist):
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    # 继续进行切分
    left = spiltSort(alist[:mid])
    right = spiltSort(alist[mid:])
    return mergeSort(left,right)
def mergeSort(left,right):
    m = len(left)
    n = len(right)
    i,j = 0,0
    result = []
    while i<m or j <n:
        if i < m and j < n:
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif i<m:
            result.append(left[i])
            i = i +1
        else:
            result.append(right[j])
            j = j + 1

    return result
alist = [54,26,93,17,77,31,44,55,20]
sorted_alist = spiltSort(alist)
print(sorted_alist)


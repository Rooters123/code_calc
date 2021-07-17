# encoding = utf-8
def binary_search(alist, item):
    if len(alist) == 0:
        return False
    mid = len(alist) // 2
    if alist[mid] == item:
        return True
    else:
        if item < alist[mid]:
            return binary_search(alist[:mid],item)
        else:
            # 这里边是要去掉中值的，因为第一次二分查找找的中值与我们要找的值是不同的
            return binary_search(alist[mid+1:],item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))

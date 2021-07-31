# encoding = utf-8
def sort_calc(alist,start,end):
    # if start >= end:
    #     return
    # low = start
    # high = end
    # mid = alist[start]
    # while low < high:
    #     while low < high and alist[high] >= mid:
    #         high -= 1
    #     alist[low] = alist[high]
    #     while low < high and alist[low] < mid:
    #         low += 1
    #     alist[high] = alist[low]
    #     # low和high重合
    #     mid = alist[low]
    #     sort_calc(alist,start,low - 1)
    #     sort_calc(alist,low + 1,end)

    if start >= end:
        return
    mid = alist[start]
    low = start
    high = end
    while low < high:
        # while low < high and alist[high] >= mid:
        while low < high and alist[high] < mid:
            high -= 1
        alist[low] = alist[high]

        while low< high and alist[low] >= mid:
            low += 1
        alist[high] = alist[low]

    alist[low] =  mid
    # print(alist)
    sort_calc(alist,start,low - 1)
    sort_calc(alist,low + 1,end)





a = [54,26,93,17,77,17,31,44,55,20]
sort_calc(a,0,len(a) - 1)
print(a)


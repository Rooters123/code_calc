# encoding = utf-8
# 构建大顶堆
import heapq
def heapify(alist,n,i):
    if i >= n :
        return
    c1 = i * 2 + 1
    c2 = i * 2 + 2
    # 类似于选择排序
    maxindex = i
    if c1 < n and alist[c1] > alist[maxindex]:
        maxindex = c1
    if c2 < n and alist[c2] > alist[maxindex]:
        maxindex = c2
    if maxindex != i:
        alist[maxindex],alist[i] = alist[i],alist[maxindex]
        heapify(alist,n,maxindex)

def buildHeap(alist):
    # 我们需要从底层往上找
    index = len(alist) - 1
    parent = (index - 1) // 2
    for i in range(parent,-1,-1):
        heapify(alist,len(alist),i)
    return alist

alist = [4,5,8,6,3,1,4]
buildHeap(alist)
print(alist) # [8, 6, 4, 5, 3, 1, 4]
for i in range(len(alist)-1,-1,-1):
    alist[0],alist[i] = alist[i],alist[0]
    # 当我们把最大值放到最后面的时候，把它从堆里移除，这里的循环从i开始就意味着从逐渐将索引最后的最大值剔除
    # 这里有一点需要注意：总是从0开始，是因为最后的值只需要从顶节点开始替换一次就可以得到最大值,
    # 因为之前最顶部的节点的字节点肯定是要比根节点小，但是要比子节点的子节点要大的
    heapify(alist,i,0)
print(alist)



#encoding = utf-8
import collections
# 给定两个数组，编写一个函数来计算它们的交集。

# 输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
# 我们可以不考虑输出结果的顺序。
# 进阶：

# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
class Solution:
    # 第一次计算

    # def intersect(self, nums1, nums2):
    #     # sort和sorted的区别就是，sort是方法，是针对原有的列表进行排序，不可逆序
    #     # sorted 是函数，因此是需要往里传参的，并且会新开辟内存空间，返回新的可迭代对象，可以设置逆序
    #     nums1.sort()
    #     nums2.sort()
    #     new_num = []
    #     i , j = 0 , 0
    #     len1 = len(nums1)
    #     len2 = len(nums2)
    #     while i < len1 and j <len2:
    #         if nums1[i] == nums2[j]:
    #             new_num.append(nums1[i])
    #             i += 1
    #             j += 1
    #
    #         elif nums1[i] > nums2[j]:
    #             j +=1
    #         else:
    #             i +=1
    #     return new_num

    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        new_list = []
        i,j = 0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                new_list.append(nums1[i])
                i += 1
                j += 1
        return new_list


s= Solution()
print(s.intersect([1,2,3,3,50],[3,5,3,5]))


# # 使用python的collections包里面的Counter函数，
print(collections.Counter([1,2,3,3,50]))
print(collections.Counter([3,5,3,5]))
#
# # Counter的&操作是取key相同,val最小的那一个
ss = collections.Counter([1,2,3,3,50]) & collections.Counter([3,5,3,5])
print([i for i in ss.elements()])



# return [x for x in set(nums1)&set(nums2) for _ in range(min(nums1.count(x),nums2.count(x)))]




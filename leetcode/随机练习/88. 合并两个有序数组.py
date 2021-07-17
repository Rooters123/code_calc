# encoding = utf-8
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 解法1：先合并，在排序
        # nums1[:] = nums1[:m] + nums2
        # 快速排序
        # self.quickSort(nums1,0,len(nums1)-1)


        #解法2
        nums1[:] = nums1[:m]
        result = []
        i,j = 0,0
        while i < len(nums1) and j <len(nums2):
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        result = result + nums1[i:]
        result = result + nums2[j:]
        nums1[:] = result
        print(nums1)

    def quickSort(self,alist,start,end):
        if start >= end:
            return alist
        midval = alist[start]
        l = start
        r = end
        while l < r:
            while l < r and alist[r] >= midval:
                r -= 1
            alist[l] = alist[r]
            while l < r and alist[l] < midval:
                l += 1
            alist[r] = alist[l]
        alist[l] = midval
        self.quickSort(alist,start,l-1)
        self.quickSort(alist,l+1,end)


s =Solution()
s.merge(nums1 = [4,5,6,0,0,0], m = 3, nums2 = [1,2,3], n = 3)

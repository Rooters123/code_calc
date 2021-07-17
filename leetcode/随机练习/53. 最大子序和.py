# encoding = utf-8
class Solution:
    def maxSubArray(self, nums):
        # 这题采用贪心算法
        if len(nums) == 1:
            return nums[0]

        two_sum = nums[0]
        maxsum = nums[0]
        for i in range(1,len(nums)):
            # 首先对two_sum进行判断是否小于0，贪心算法是要舍弃和小于0的值，替换为0
            two_sum = max(two_sum,0)
            # 前后数值相加
            two_sum = two_sum + nums[i]
            maxsum = max(two_sum,maxsum)

        return maxsum
s = Solution()
alist = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(alist))



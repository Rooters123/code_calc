#encoding = utf-8
# 给定一个整数数组，判断是否存在重复元素。
#
# 如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
class Solution:
    def maxProfit(self, nums):
        # 第一种解法，对数组进行排序，如果相邻两个元素相同，那么就代表存在重复值
        # nums.sort()
        # for i in range(len(nums) - 1 ):
        #     if nums[i] == nums[i + 1] :
        #         return True
        # return False

        #第二种解法：利用python的集合进行自动去重
        # print(set(nums))
        # return len(nums) != len(set(nums))

        # 第三种：
        nums = "".join(str(s) for s in nums)
        print(nums)
        for i in range(len(nums)):
            if nums.find(nums[i]) != nums.rfind(nums[i]):
                return False
        return True


s = Solution()
print(s.maxProfit([1,2,3,4,4]))

#encoding = utf-8

class Solution:
    def twoSum(self, nums, target):
        # 第一种解法
        # for i in range(len(nums) - 1):
        #     if (target - nums[i]) in nums[i + 1:]:
        #         return [i, nums[i + 1:].index(target - nums[i]) + i + 1]
        # 第二种解法
        hashtable = dict()
        for i in range(len(nums)):
            if (target - nums[i]) in hashtable:
                return [i,hashtable[target - nums[i]]]
            hashtable[nums[i]] = i

    def twoSum2(self,nums,target):
        for i in range(len(nums) - 1):
            subnum = target - nums[i]
            if subnum in nums[i+1:]:
                return i,nums[i+1:].find(subnum)
        return []
s =Solution()
print(s.twoSum([1,3,3,3,3],6))

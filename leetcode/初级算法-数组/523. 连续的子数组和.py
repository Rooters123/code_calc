# encoding = utf-8
# 给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：
# 注意这里是连续的子数组
# 子数组大小 至少为 2 ，且子数组元素总和为 k 的倍数。
class Solution:
    def checkSubarraySum(self, nums, k):
        # 同余定理和前缀和
        # 要使得两者除k相减为整数，需要满足sum[j]和sum[i−1] 除k余数相同。
        pre = 0
        hashdic = dict()
        hashdic[0] = -1
        for i in range(len(nums)):
            pre = pre + nums[i]
            rem = pre % k
            if rem not in hashdic:
                hashdic[rem] = i
            elif i -  hashdic[rem] <= 1:
                continue
            else:
                return True
        return False

nums = [23,2,4,6,7]
s =Solution()
print(s.checkSubarraySum(nums,6))
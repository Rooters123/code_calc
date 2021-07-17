#encoding = utf-8
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 进阶：
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
class Solution:
    def maxProfit(self, nums, k):
        # 当 k 很大，数组长度较小。如 k = 100,len(nums) = 5,数组切片会出问题吧
        k = k % len(nums)
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]


        # new_list = nums[len(nums) - k:]
        # new_list.extend((nums[:len(nums) - k]))
        # print(new_list)
        return nums
s= Solution()
print(s.maxProfit([1,3,46,4,6,65,7],3))


#encoding = utf-8
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
class Solution:
    def moveZeroes(self, nums):
        # 1、不合格的写法，这样会修改数组的值
        # 给定一个数组nums，编写一个函数将所有0移动到数组的末尾，同时保持非零元素的相对顺序。
        # index = 0
        # for i in nums:
        #     if i == 0:
        #         nums.remove(i)
        #         index += 1
        # nums += ([0] * index)

        # 2、双指针
        # i是快指针，j是慢指针，慢指针是用来记录0的索引位置
        # 扩展：将奇数偶数分开
        j = 0
        for i in range(len(nums)):
            if (nums[i] % 2) != 0:
                nums[j],nums[i] = nums[i],nums[j]
                j +=1
            # print(nums)
        return nums

    def moveZeroes2(self,nums):
        slow = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[slow] = nums[slow],nums[i]
                slow += 1
        return nums

s= Solution()
print(s.moveZeroes2([1,0,3,12,0,2,5]))
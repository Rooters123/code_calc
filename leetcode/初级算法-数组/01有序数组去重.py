#encoding = utf-8
# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。


# 0 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104
# nums 已按升序排列

class Solution:
    def removeDuplicates(self, nums):
        #快慢指针
        # 这种解法只是计算了去重数组的长度，本质上并没有将重复元素删除。
        slow= 0
        for fast in range(1,len(nums)):
            if nums[slow] != nums[fast]:
                slow = slow + 1
                nums[slow] = nums[fast]
        print(nums)
        return slow + 1

    slow = 0




s = Solution()
# print(s.removeDuplicates([2,3,3,3,5]))
alist = [2,3,3,3,5]
slow = 0
for i in range(1, len(alist)):
    if alist[slow] != alist[i]:
        slow += 1
    alist[slow] = alist[i]
print(alist[0:slow + 1])
# encoding = utf-8
class Solution:
    def removeElement(self,nums,val):
        slow = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i],nums[slow] = nums[slow],nums[i]
                slow += 1
        return nums[:slow]
s =Solution()
print(s.removeElement([3,2,2,3],3))


#encoding = utf-8
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 使用异或运算，将所有值进行异或
# 异或运算，相异为真，相同为假，所以 a^a = 0 ;0^a = a
# 因为异或运算 满足交换律 a^b^a = a^a^b = b 所以数组经过异或运算，单独的值就剩下了

class Solution:
    def singleNumber(self, nums):
        result = 0
        for i in range(len(nums)):
            result ^= nums[i]
        return result
s= Solution()
print(s.singleNumber([1,3,3,1,8]))
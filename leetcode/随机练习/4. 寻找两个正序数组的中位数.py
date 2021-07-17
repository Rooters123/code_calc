# encoding = utf-8
class Solution:
    def findMedianSortedArrays(self,num1,num2):
        num = num1 + num2
        num.sort()
        if len(num) % 2 == 0:
            return float ((num[len(num) // 2] + num[(len(num) // 2) - 1]) / 2)
        else:
            return float(num[len(num) // 2])
s =Solution()
print(s.findMedianSortedArrays([1],[]))
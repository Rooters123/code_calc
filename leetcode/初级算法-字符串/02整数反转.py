# encoding = utf-8
class Solution:
    def reverse(self, x):
        if x < 0:
            s= str(x)[1:]
            s = s[::-1]
            return 0 if -int(s) < -(2**31)+1 else -int(s)
        else:
            s = str(x)
            s = s[::-1]
            return 0 if int(s) > (2 ** 31) else int(s)
s = Solution()
print(s.reverse(-123))

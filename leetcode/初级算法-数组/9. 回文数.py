# encoding = utf-8
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = list(str(x))
        n = len(str_x)
        mid = n // 2
        for i in range(mid):
            if str_x[i] != str_x[n-i-1]:
                return False
        return True
s = Solution()
print(s.isPalindrome(101))
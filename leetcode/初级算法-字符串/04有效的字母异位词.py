# encoding = utf-8
class Solution:
    def isAnagram(self, s, t):
        # s= list(s)
        # t =list(t)
        # s.sort()
        # t.sort()
        # if len(s) == len(t):
        #     for i in range(len(s)):
        #         if s[i] != t[i]:
        #             return False
        #     return True
        # return False
        return sorted(list(s)) == sorted(list(t))
s = Solution()
print(s.isAnagram("rat","car"))

print("rat" == "ra")


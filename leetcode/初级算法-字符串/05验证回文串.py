# encoding = utf-8
class Solution:
    def isPalindrome(self, s):
        new_str = "".join([ch.lower() for ch in s if ch.isalnum()])
        return new_str[::-1]
s= Solution()
print(s.isPalindrome(["A man, a plan, a canal: Panama"]))

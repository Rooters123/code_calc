# encoding = utf-8
class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()
        space_index = s.split(" ")
        return len(space_index[-1])

s = Solution()
print(s.lengthOfLastWord("a "))
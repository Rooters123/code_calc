# encoding = utf-8
import re
class Solution:
    def strStr(self, haystack, needle):
        # find在寻找的过程中是，如果不存在则会返回-1
        # return haystack.find(needle) if haystack.find(needle)>-1 else 0
        # index如果不存在子字符串，会报错
        # return haystack.index(needle)

        # 类似于str.find的作用
        s1 = len(haystack)
        s2 = len(needle)
        if s2 ==0:
            return 0
        i, j = 0, 0
        while i < s1 and j < s2:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                i = i - j + 1
                j = 0
        return i-j if j == s2 else -1




s =Solution()
print(s.strStr("hello","o"))

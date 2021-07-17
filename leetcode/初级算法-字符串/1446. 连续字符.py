# encoding = utf-8
class Solution:
    def maxPower(self, s):
        ss = list(s)
        if len(ss) == 1 :return 1
        i = 0
        j = 1
        count = 1
        while j < len(ss):
            if ss[i] != ss[j]:
                count = max(count,j - i)
                i = j
                j += 1
            else:
                j += 1
        # 处理一下末尾的连续字符
        if ss[i] == ss[j - 1]:
            count = max(count, j - i)
        print(count)

s =Solution()
s.maxPower(s = "bcc")
from collections import Counter
# strs =  "yxdxwnjstjqqdgauhnfffasdwasffd"
# s.maxPower(strs)
# print(Counter(strs))
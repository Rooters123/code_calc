# encoding = utf-8
# 字符串中的第一个唯一字符
class Solution:
    def firstUniqChar(self, s):
        # 错误的解法 "dddccdbba"
        # s = list(s)
        # if len(s) == 1:
        #     return 0
        # for i in range(len(s) -1):
        #     print(s[0:i] + s[i+1:])
        #     if s[i] not in (s[0:i] + s[i+1:]):
        #         print(s[i+1:])
        #         return s.index(s[i])
        # return -1

        # (2)字典加集合

        # dict = {c:s.count(c) for c in set(s)}
        # # 字典是无序的
        # print(dict)
        # for index,val in enumerate(s):
        #     if dict[val] == 1:
        #         return index
        # return -1

        # (3)字符查找
        max_index = len(s)
        for i in range(len(s)):
            index = s.find(s[i])
            if index!=-1 and s.rfind(s[i]) == index:
                return index
                # max_index = min(max_index,index)
        return -1 if max_index==len(s) else max_index




s = Solution()
print(s.firstUniqChar("aabbccde"))

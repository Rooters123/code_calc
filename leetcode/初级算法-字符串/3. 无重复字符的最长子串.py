# encoding = utf-8
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        # 解法1：
        # tmp = {}
        # left = 0
        # ret = 0
        # for i, j in enumerate(s):
        #     if j in tmp:
        #         # 如果重复的数字出现在l之前忽略，否则了跳到该值的下一个位置
        #         # 如果不加max条件，abba会导致在计算a的时候指针回退
        #         left =max(left,tmp[j] + 1)
        #     tmp[j] = i
        #     ret = max(ret, i - left + 1)
        # return ret
        # 解法2：
        pass
        # 解法二
        # if not s :return 0
        # max_len = 0
        # tp = []
        # for i in s:
        #     while i in tp:
        #         del tp[0]
        #     tp.append(i)
        #     max_len = max(max_len,len(tp))
        # return max_len

        if not s : return 0
        max_len = 0
        result = []
        for i in s:
            while i in result:
                del result[0]
            result.append(i)
            max_len = max(max_len,len(result))
        return result

strs = "abcadaefa"
s =Solution()
print(s.lengthOfLongestSubstring(strs))
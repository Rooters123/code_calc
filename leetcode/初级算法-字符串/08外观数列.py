# encoding = utf-8
class Solution:
    def countAndSay(self, n):
        s = "1"
        for i in range(n):
            i, j = 0, 0
            key , val = [] , []
            while i < len(s) and j < len(s):
                if s[i] == s[j]:
                    if i == (len(s) - 1):
                        key.append(s[j])
                        val.append(i - j + 1)
                        i += 1
                    else:
                        i += 1
                else:
                    key.append(s[j])
                    val.append(i - j)
                    j = i
            s = "".join([str(val[k]) + v  for k,v in enumerate(key)])
        return s
        # i, j = 0, 0
        # key, val = [], []
        # while i < len(s) and j < len(s):
        #     if s[i] == s[j]:
        #         if i == (len(s) - 1):
        #             key.append(s[j])
        #             val.append(i - j + 1)
        #             i += 1
        #         else:
        #             i += 1
        #     else:
        #         key.append(s[j])
        #         val.append(i - j)
        #         j = i
        # print(key)
        # print(val)
s =Solution()
s.countAndSay(4)

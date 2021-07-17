# encoding = utf-8
import re
class Solution:
    def myAtoi(self, s):
        # 正则表达式
        # max(min(数字, 2 ** 31 - 1), -2 ** 31)
        s= s.lstrip()
        new_str = re.findall(r"^[\+\-]?\d+",s)
        return max(min(int(*new_str),2 ** 31 - 1),-2**31)



s = Solution()
print(s.myAtoi("-w546asd-2"))


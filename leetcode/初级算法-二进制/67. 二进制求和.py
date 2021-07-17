# encoding = utf-8
import math
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        p = 0
        r = ''
        add_zero = len(a) - len(b)
        a = '0' * -add_zero + a
        b = '0' * add_zero + b
        for i,j in zip(a[::-1],b[::-1]):
            num = int(i) + int(j) + p
            p = num // 2
            cur_num = num % 2
            r = str(cur_num) + r
        return '1' + r if p == 1 else r



# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         r, p = '', 0
#         d = len(b) - len(a)
#         a = '0' * d + a
#         b = '0' * -d + b
#         for i, j in zip(a[::-1], b[::-1]):
#             s = int(i) + int(j) + p
#             r = str(s % 2) + r
#             p = s // 2
#         return '1' + r if p else r
s = Solution()
print(s.addBinary('1010','1011'))


print(math.log(2))
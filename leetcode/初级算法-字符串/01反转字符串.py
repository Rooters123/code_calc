# encoding = utf-8

# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

# 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        # 第一种解法：Python一行代码
        # s.reverse()
        # if len(s) % 2 == 0:
        #     num = len(s) // 2
        # else:
        #     num = (len(s) // 2) + 1
        for i in range(0,len(s) // 2):
            s[i] , s[len(s) - i - 1]  = s[len(s) - i - 1] ,s[i]
        print(s)
s = Solution()
s.reverseString(["a","b","c","e","f"])
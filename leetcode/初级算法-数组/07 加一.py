#encoding = utf-8
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

# 你可以假设除了整数 0 之外，这个整数不会以零开头。

# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# 这里需要考虑的是数组是[9,9] 进行加一之后是需要进位的
# 这时候可以将数字转换为字符串
class Solution:
    def plusOne(self, digits):
        # 第一种解法：使用字符串来进行解析
        # nums = int("".join([str(i) for i in digits]))
        # nums += 1
        # return [s for s in str(nums)]

        # 第二种：利用进位的关系
        digits = [0] + digits
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
        if digits[0] == 0:
            return digits[1:]
        else:
            return digits


    def plusOne2(self,digits):
        digits.insert(0,0)
        for i in range(len(digits)-1,-1,-1):
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                return  digits[1:]
            else:
                digits[i] = 0




s= Solution()
print(s.plusOne2([0]))
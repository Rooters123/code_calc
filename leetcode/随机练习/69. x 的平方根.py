# encoding = utf-8
class Solution:
    def mySqrt(self, x: int) -> int:
        # 方法1：二分查找
        left = 0
        right = x
        temp = -1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                left = mid + 1
                temp = mid
            else:
                right = mid - 1
        return temp
        # 方法二：牛顿迭代法
        # if x == 0:
        #     return 0
        # C, x0 = float(x), float(x)
        # while True:
        #     xi = 0.5 * (x0 + C / x0)
        #     if abs(x0 - xi) < 1e-7:
        #         break
        #     x0 = xi
        # return int(x0)
s = Solution()
print(s.mySqrt(25))
# encoding = utf-8
import functools
class Solution:
    # 必须加这个缓存机制，不然过不了leetcode
    @functools.lru_cache(maxsize=128)
    def climbStairs(self, n):
        # 假设你正在爬楼梯。需要n阶你才能到达楼顶。
        # 每次你可以爬1或2个台阶。你有多少种不同的方法可以爬到楼顶呢？
        # 通过分析可以发现，f(n) = f(n-1) + f(n-2)
        # 因为爬上第n阶楼梯，只能由第n-1阶楼梯再上一阶，或者n-2阶楼梯再上两级阶

        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)

s = Solution()
print(s.climbStairs(15))

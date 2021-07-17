#encoding = utf-8
# 1 <= prices.length <= 3 * 104
# 0 <= prices[i] <= 104
class Solution:
    def maxProfit(self, prices):
        sum = 0
        for i in range(len(prices)):
            if prices[i+1] - prices[i] >0:
                sum =sum + prices[i+1] - prices[i]
        return sum



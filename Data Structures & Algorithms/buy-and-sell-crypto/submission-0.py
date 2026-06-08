class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost = prices[0]
        profit = 0
        for i in prices[1:]:
            if i < cost:
                cost = i
            else:
                currprofit = i - cost
                profit = max(profit, currprofit)
        return profit

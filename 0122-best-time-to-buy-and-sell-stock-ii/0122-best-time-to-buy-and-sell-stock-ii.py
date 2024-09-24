class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        start = prices[0]     
        maxProfit = 0

        for i in range(0, len(prices)):
            if start < prices[i]:
                maxProfit += prices[i] - start
            start = prices[i]
        return maxProfit

        # greedy algo works because the problem allows same-day trading, meaning you can sell and immediately buy back on the same day. This flexibility ensures that the greedy approach works perfectly because it lets you capture every price increase, even if the increases happen close together or even on consecutive days.
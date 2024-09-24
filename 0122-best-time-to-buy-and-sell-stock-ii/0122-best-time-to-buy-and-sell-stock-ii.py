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
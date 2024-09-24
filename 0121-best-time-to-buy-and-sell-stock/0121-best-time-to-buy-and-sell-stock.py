class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        r = 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                currentProfit = prices[r] - prices[l]
                maxProfit = max(currentProfit, maxProfit)
            else:
                l = r # bc now a new low is find, shift l to                    to new low
            r += 1
        return maxProfit
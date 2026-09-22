class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum =prices[0]
        profit = 0 
        best_profit =0
        for i in prices:
            if i < minimum:
                minimum = i
            else:
                profit = i - minimum 

            if profit > best_profit:
                best_profit = profit
            else:
                pass
            
        return best_profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        profit = 0 

        for price in prices:
            smallest = min(price, smallest)
            profit = max(price - smallest, profit)
        
        return profit
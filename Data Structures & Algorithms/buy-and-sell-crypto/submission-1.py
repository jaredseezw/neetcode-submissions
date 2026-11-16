class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #pair largest value with index
        smallest = (float("inf"), 0)
        highest = (0, 0)
        difference = 0
    
        for i in range(len(prices)):
            # always update highest
            if prices[i] >= highest[0]:
                highest = (prices[i], i)
            #if smaller than smallest
            if prices[i] <= smallest[0]:
                difference = max(difference, highest[0] - smallest[0])
                smallest = highest = (prices[i], i)

        if highest[1] > smallest[1]:
            return max(difference, highest[0]-smallest[0])
        return difference
                
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largest = 0

        #Set the largest
        for p in piles:
            largest = max(p, largest)
        
        #helper to return a bool if can clear the pile within h
        def check_Clear(rate) -> bool:
            hours = 0
            for p in piles:
                hours += (p + rate - 1) // rate

            return hours <= h
        
        lowest = 1

        while lowest <= largest:
            mid = lowest + (largest - lowest) // 2

            if check_Clear(mid):
                largest = mid - 1
            else:
                lowest = mid + 1
            
        return lowest
        
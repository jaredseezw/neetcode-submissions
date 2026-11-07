class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        minimum = nums[0]

        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] > nums[high]:#rotation exists
                low = mid + 1
            
            else:
                minimum = min(minimum, nums[mid])
                high = mid - 1
                
        return minimum

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(array, target):
            low = 0
            high = len(array) - 1

            while low <= high:
                mid = low + (high - low) // 2
                if array[mid] == target:
                    return True
                elif array[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return False
        
        #Binary Search on arrays
        low = 0 
        high = len(matrix) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return binarySearch(matrix[mid], target)
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
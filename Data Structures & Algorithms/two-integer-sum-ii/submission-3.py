class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #max will be last index, min will be first index
        i = 0
        j = len(numbers) - 1

        while i <= j:
            left = target - numbers[i]
            if numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[j] > target: 
                j -= 1
            else:
                i += 1
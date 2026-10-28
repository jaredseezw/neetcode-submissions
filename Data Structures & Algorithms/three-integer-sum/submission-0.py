class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(numbers: List[int], target: int) -> List[int]:
            #max will be last index, min will be first index
            i = 0
            j = len(numbers) - 1

            while i < j:
                left = target - numbers[i]
                if numbers[j] == left:
                    return [numbers[i], numbers[j]]
                elif numbers[j] > left: 
                    j -= 1
                else:
                    i += 1
            
        ans = []
        for i in range(len(nums) - 2):
            # nums[i] stays fixed during this search
            left = i + 1
            right = len(nums) - 1

            # Find two numbers whose sum equals -nums[i]
            result = twoSum(nums[left: right], 0 - (nums[i]))
            if result:
                ans.append([nums[i], result[0], result[1]])
        return ans
            

    
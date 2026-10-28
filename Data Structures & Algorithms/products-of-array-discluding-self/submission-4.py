class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length

        prefix = 1
        for i in range(length):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for j in range(length - 1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
        return res
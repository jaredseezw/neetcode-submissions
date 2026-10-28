class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ret = [1] * l

        prefix = nums[0]
        for i in range(1, l):
            ret[i] = prefix 
            prefix *= nums[i]

        postfix = nums[l - 1]
        for j in range(l - 2, - 1, - 1):
            ret[j] = postfix
            postfix *= ret[j]
        
        return ret
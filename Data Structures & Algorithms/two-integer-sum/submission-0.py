class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in hashtable:
                return [hashtable[needed], i]
            hashtable[nums[i]] = i
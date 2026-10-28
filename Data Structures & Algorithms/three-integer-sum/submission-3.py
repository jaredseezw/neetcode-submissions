class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        ans = []
        
        for i in range(length - 2):
            j = i + 1
            k = length - 1
            left = 0 - nums[i]

            while j < k:
                if nums[j] + nums[k] == left:
                    if ans and ans[-1] != [nums[i], nums[j], nums[k]]:
                        ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < left:
                    j += 1
                elif nums[j] + nums[k] > left:
                    k -= 1

        return ans
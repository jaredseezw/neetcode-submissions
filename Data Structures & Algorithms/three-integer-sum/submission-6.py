class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        ans = []
        hashtable = set()
        
        for i in range(length - 2):
            j = i + 1
            k = length - 1
            left = 0 - nums[i]

            while j < k:
                if nums[j] + nums[k] == left:
                    if (nums[i], nums[j], nums[k]) in hashtable:
                        j += 1
                        k -= 1
                        continue;
                        
                    ans.append([nums[i], nums[j], nums[k]])
                    hashtable.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < left:
                    j += 1
                elif nums[j] + nums[k] > left:
                    k -= 1

        return ans
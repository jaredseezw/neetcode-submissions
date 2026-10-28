class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashtable = set()
        for n in nums:
            if n in hashtable:
                return True
            hashtable.add(n)
        return False
        
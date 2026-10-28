class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Hashtable, then check if n-1 exist? store the counter
        hashtable = {}
        max_counter = 0

        #Loop through arr
        for n in nums:
            left = hashtable.get(n - 1, 0)
            right = hashtable.get(n + 1, 0)
            if n in hashtable:
                continue;
            elif n - 1 in hashtable and n + 1 in hashtable:
                hashtable[n] = hashtable[n - 1] + hashtable[n + 1] + 1
            elif n - 1 in hashtable:
                hashtable[n] = hashtable[n - 1] + 1
            elif n + 1 in hashtable:
                hashtable[n] = hashtable[n + 1] + 1
            else:
                hashtable[n] = 1
            #Update max_counter
            if hashtable[n] > max_counter:
                    max_counter = hashtable[n]
            #Update bondaries
            hashtable[n - left] = hashtable[n]
            hashtable[n + right] = hashtable[n]     

        return max_counter

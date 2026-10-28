class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = {}
        freq_Array = [[] for _ in range(len(nums) + 1)]
        #Loop through and hash, increasing count
        for n in nums:
            hashtable[n] = hashtable.get(n, 0) + 1
        for number, frequency in hashtable.items():
            freq_Array[frequency].append(number)

        array = []
        start = len(freq_Array) - 1
        elements = k

        while elements > 1:
            for n in freq_Array[start]:
                array.append(n)
                elements -= 1
            start -= 1
            
        return array

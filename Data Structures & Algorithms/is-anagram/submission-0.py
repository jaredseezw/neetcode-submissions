class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        for letter in s:
            if letter in countS:
                countS[letter] += 1
            else:
                countS[letter] = 1
        for letter in t:
            if letter in countT:
                countT[letter] += 1
            else:
                countT[letter] = 1
        return countT == countS
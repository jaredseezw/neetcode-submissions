class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s: str, t: str) -> bool:
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
        #Make a array when see new element / add to existing hash
        array = []
        for s in strs:
            found = False
            for i in array:
                if isAnagram(s, i[0]) and found == False:
                    i.append(s)
                    found = True
                    break;
            if found == False:
                array.append([s])

        return array
                
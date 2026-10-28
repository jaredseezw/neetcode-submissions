class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            #if both alphabet, check and if != return false
            if s[i].isalpha() and s[j].isalpha() and s[i].lower() != s[j].lower():
                return False
            # if s[i] is not the alphabet, change i 
            elif not s[i].isalpha():
                i += 1
            
            elif not s[j].isalpha():
                j -= 1
            else:
                i += 1
                j -= 1
        return True
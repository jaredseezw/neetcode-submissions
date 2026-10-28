class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        j = length - 1
        for i in range(length):
            if s[i].isalpha() and s[j].isalpha() and s[i] != s[j]:
                return False
            elif not s[i].isalpha():
                continue;
            else: 
                j -= 1
        return True
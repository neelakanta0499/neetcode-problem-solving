class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = ""
        for c in s:
            if c.isalnum():
                alphanum += c.lower()
        i = 0
        j = len(alphanum)-1
        while i < j:
            if alphanum[i] != alphanum[j]:
                return False
            i += 1
            j -= 1
        return True
        
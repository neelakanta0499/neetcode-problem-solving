class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = len(s)-1
        j = len(t)-1
        while i >= 0 and j >= 0:
            if s[i] == t[j]:
                i -= 1
            j -= 1
        return i < 0
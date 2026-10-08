class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = "".join(sorted(s))
        t = "".join(sorted(t))

        i = len(s)-1
        j = len(t)-1
        while i >= 0 and j >= 0:
            if s[i] != t[j]:
                return False
            i -= 1
            j -= 1
        return j == i

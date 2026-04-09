class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        zeros = 0
        ones = s.count("1")
        i = 0
        while i < len(s)-1:
            if s[i] == "0":
                zeros += 1
            elif s[i] == "1":
                ones -= 1
            res = max(res, zeros+ones)
            i += 1
        return res
class Solution:
    def maxScore(self, s: str) -> int:
        res = count = 0
        for i in range(1, len(s)):

            count = s[:i].count("0") + s[i:].count("1")
            res = max(res, count)
        return res
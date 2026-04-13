class Solution:
    def maxScore(self, s: str) -> int:
        # res = count = 0
        # for i in range(1, len(s)):
        #     count = s[:i].count("0") + s[i:].count("1")
        #     res = max(res, count)
        # return res
        res = 0
        ones = s.count("1")
        zeros = 0
        i = 0
        while i < len(s)-1:
            if s[i] == "0":
                zeros += 1
            elif s[i] == "1":
                ones -= 1
            res = max(res, zeros + ones)
            i += 1
        return res
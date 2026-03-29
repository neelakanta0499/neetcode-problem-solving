class Solution:
    def minOperations(self, s: str) -> int:
        alt_1 = 0
        alt_2 = 0

        for i in range(len(s)):
            if s[i] == str(i % 2):
                alt_1 += 1
            elif s[i] == str((i+1) % 2):
                alt_2 += 1
        return min(alt_1, alt_2)
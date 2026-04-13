class Solution:
    def minOperations(self, s: str) -> int:
        alt_0 = alt_1 = 0
        for i in range(len(s)):
            if s[i] == str(i%2):
                alt_0 += 1
            elif s[i] == str((i+1)%2):
                alt_1 += 1
        return min(alt_0, alt_1)
            
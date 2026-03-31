class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        max_odd = float("-inf")
        min_even = float("inf")
        for val in freq.values():
            if val % 2:
                max_odd = max(val, max_odd)
            else:
                min_even = min(val, min_even)
        return max_odd - min_even
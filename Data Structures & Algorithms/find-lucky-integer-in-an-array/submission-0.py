class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        res = -1
        for key, val in freq.items():
            if key == val:
                res = max(val, res)
        return res
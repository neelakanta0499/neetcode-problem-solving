class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res = 0
        for val in freq.values():
            res += val * (val-1) // 2
        return res
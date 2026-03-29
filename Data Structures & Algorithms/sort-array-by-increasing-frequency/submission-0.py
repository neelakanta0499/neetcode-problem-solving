class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        res = []
        for key, val in sorted(freq.items(), key=lambda x: (x[1], -x[0])):
            for _ in range(val):
                res.append(key)
        return res


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        for item in arr:
            freq[item] = freq.get(item, 0) + 1
        for key, val in freq.items():
            if val == 1:
                k -= 1
            if k == 0:
                return key
        return ""
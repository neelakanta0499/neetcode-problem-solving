class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [num*num for num in nums]
        return sorted(arr)
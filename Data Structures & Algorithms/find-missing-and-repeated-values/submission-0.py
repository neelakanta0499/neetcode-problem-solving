class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        freq = {}
        n = len(grid)
        for i in range(n):
            for j in range(n):
                freq[grid[i][j]] = freq.get(grid[i][j], 0) + 1
        for num in range(1, (n*n)+1):
            if num not in freq:
                missing = num
            elif freq[num] >= 2:
                double = num
        return [double, missing]
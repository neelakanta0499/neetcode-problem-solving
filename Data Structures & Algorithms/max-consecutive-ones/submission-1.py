class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = total = 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                cnt = 0
            total = max(cnt, total)
        return total
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]

        for i in range(len(nums)):
            l = nums[i-1] if i else 0
            r = nums[-1] - nums[i]
            if l == r:
                return i
        return -1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = R = 1
        while R < len(nums):
            if nums[L-1] != nums[R]:
                nums[L] = nums[R]
                L += 1
            R += 1
        return L
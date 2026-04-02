class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        """count = nums[0]
        res = 0
        flag = False
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                count += nums[i]
                flag = True
            else:
                count = nums[i]
            res = max(res, count)
        return res if flag else nums[0]"""

        count = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                count = 0
            count += nums[i]
            res = max(res, count)
        return res
            
            
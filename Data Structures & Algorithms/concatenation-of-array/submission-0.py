class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        con_arr = [0]*len(nums)*2
        for i in range(len(nums)):
            con_arr[i] = con_arr[len(nums)+i] = nums[i]
        return con_arr
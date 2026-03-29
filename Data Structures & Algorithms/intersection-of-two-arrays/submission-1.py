class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return list(set(nums1) & set(nums2))

        count_nums1 = Counter(nums1)
        count_nums2 = Counter(nums2)
        res = []
        for num in count_nums1:
            if num in count_nums2:
                res.append(num)
        return res
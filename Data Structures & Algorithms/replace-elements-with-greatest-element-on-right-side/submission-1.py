class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        grt_ele_so_far = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            ele = arr[i]
            arr[i] = grt_ele_so_far
            if ele > grt_ele_so_far:
                grt_ele_so_far = ele

        return arr

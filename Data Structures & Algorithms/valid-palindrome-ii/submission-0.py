class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(arr, l, r):
            
            while l < r:
                if arr[l] != arr[r]:
                    return False
                l += 1
                r -= 1
            return True
        i = 0
        j = len(s) -1
        while i < j:
            if s[i] != s[j]:
                return isPalindrome(s, i+1, j) or isPalindrome(s, i, j-1)
            i += 1
            j -= 1
        return True

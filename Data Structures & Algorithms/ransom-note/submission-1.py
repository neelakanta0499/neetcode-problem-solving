class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countRans = Counter(ransomNote)
        countMag = Counter(magazine)
        for c in ransomNote:
            if countRans[c] > countMag[c]:
                return False
        return True
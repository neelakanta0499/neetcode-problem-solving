class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        string = ""
        for word in words:
            string += word
        freq = Counter(string)

        for val in freq.values():
            if val % len(words):
                return False
        return True
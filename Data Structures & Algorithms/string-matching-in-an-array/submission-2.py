class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for word in words:
            for match_w in words:
                if word == match_w:
                    continue
                if word in match_w:
                    if res and res[-1] == word:
                        continue
                    res.append(word)
        return res
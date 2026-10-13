class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for word in words:
            for match_w in words:
                if word == match_w:
                    continue
                if word in match_w:
                    res.append(word)
                    break
        return res
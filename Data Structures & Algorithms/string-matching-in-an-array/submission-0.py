class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for check_word in words:
            for word in words:
                if check_word == word:
                    continue
                elif check_word in word:
                    res.append(check_word)
                    break
        return res
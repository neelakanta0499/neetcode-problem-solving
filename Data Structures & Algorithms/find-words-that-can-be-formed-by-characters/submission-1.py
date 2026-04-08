class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counterChars = Counter(chars)
        res = 0
        for word in words:
            freq_char = defaultdict(int)
            is_good = True
            for c in word:
                freq_char[c] = freq_char.get(c, 0)+1
                if c not in counterChars or freq_char[c] > counterChars[c]:
                    is_good = False
                    break
            if is_good:
                res += len(word)
        return res
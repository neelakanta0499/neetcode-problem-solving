class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter('balloon')
        counterText = Counter(text)
        res = len(text)
        for c in balloon:
            res = min(res, counterText[c]//balloon[c])
        return res
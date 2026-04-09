class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = 0
        result = ""
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                temp = num[i:i+3]
                if int(temp) >= res:
                    res = int(temp)
                    result = temp
        return result
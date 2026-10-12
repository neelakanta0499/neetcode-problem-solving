class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for each_person_info in details:
            if int(each_person_info[11:13]) > 60:
                cnt += 1
        return cnt
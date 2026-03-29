class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for each_person_detail in details:
            if int(each_person_detail[11:13]) > 60:
                count += 1
        return count
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            sort_w = "".join(sorted(word))
            res[sort_w].append(word)
        return list(res.values())
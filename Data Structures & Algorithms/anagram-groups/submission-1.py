class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            sort_word = "".join(sorted(word))
            hashmap[sort_word].append(word)
        return list(hashmap.values())
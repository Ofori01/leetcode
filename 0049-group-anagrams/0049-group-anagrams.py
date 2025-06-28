class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use dict and sort keys
        res  = defaultdict(list)

        for word in strs:
            res["".join(sorted(word))].append(word)
        return [res[ans] for ans in res]



        
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0]*len(s)

        for i,v in enumerate(indices):
            res[v] = s[i]
        return ''.join(res)

        
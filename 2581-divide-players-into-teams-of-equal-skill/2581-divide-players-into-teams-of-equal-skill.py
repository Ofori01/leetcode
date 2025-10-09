class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # sort and use 2 pointers from the ends and compare

        skill.sort()

        s= skill[0] + skill[len(skill)-1]
        res = skill[0] * skill[len(skill)-1]
        l , r = 1, len(skill) -2

        while l < r:
            if skill[l] + skill[r] != s:
                return -1
            res+=skill[l] * skill[r]
            l+=1
            r-=1
        return res


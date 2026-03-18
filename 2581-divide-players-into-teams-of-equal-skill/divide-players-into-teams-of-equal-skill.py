class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill) - 1
        t = skill[l] + skill[r]
        c = 0
        while l < r:
            if skill[l] + skill[r] != t:
                return -1
            c += skill[l] * skill[r]
            l += 1
            r -= 1
        return c
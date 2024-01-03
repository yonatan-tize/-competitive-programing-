class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        team = skill[0] + skill[-1]
        count = 0
        l, r = 0, len(skill)-1
        while l < r:
            if skill[l] + skill[r] == team:
                count += (skill[l] * skill[r])
            else:
                return -1
            l += 1
            r -= 1
        return count


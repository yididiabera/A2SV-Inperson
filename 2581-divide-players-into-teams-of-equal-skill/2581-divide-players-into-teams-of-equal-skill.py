class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        l, r = 0, len(skill) - 1
        total_chemistry = 0

        target = skill[l] + skill[r]

        while l < r:
            if skill[l] + skill[r] != target:
                return -1
            total_chemistry += skill[l] * skill[r]
            l += 1
            r -= 1

        return total_chemistry
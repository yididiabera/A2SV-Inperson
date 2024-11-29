class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        #first sort the skill
        #intialize left and right ptrs one at the beginning of the array and one at the end the array
        #compute target skill sum using the new two ptrs
        #pair players and check if the violate the condition(not equal to our target) if not add the product to the total chemistry
        skill.sort()
        l, r = 0, len(skill) - 1
        target = skill[l] + skill[r]
        total_chemistry = 0

        while l < r:
            if skill[l] + skill[r] != target:
                return -1
            total_chemistry += skill[l] * skill[r]
            l += 1
            r -= 1
        return total_chemistry
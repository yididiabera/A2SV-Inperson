class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pmap = {}
        for index, value in enumerate(nums):
            dif = target - value
            if dif in pmap:
                return [pmap[dif], index]
            pmap[value] = index
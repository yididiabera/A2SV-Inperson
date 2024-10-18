class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        total = 0

        for n in nums:
            total += n
            result.append(total)
        return result

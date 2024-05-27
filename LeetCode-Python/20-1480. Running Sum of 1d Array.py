class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        length = len(nums)

        for i in range(length):
            result.append(nums(nums[: i + 1]))
        return result
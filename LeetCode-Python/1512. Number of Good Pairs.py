class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        length = len(nums)
        for i in range(length):
            for j in range(length):
                if nums[i] == nums[j] and (i < j):
                    count += 1
        return count
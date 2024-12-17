class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        result = []
        n = len(nums)
        for i in range(n):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        for n in freq:
            if freq[n] == 2:
                result.append(n)
        return result
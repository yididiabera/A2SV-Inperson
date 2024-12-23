class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _max = -1
        l, r = 0, 1
        while r < len(nums):
            if nums[r] > nums[l]:
                _max = max(_max, nums[r] - nums[l])
            else:
                l = r
            r += 1
        return _max
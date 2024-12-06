class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _max = nums[0]
        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            _max = max(_max, curSum)
        return _max

        # _max = 0
        # for i in range(len(nums)):
        #     _sum = 0
        #     for j in range(i, len(nums)):
        #         _sum += nums[j]
        #         _max = max(_max, _sum)
        # return _max
        

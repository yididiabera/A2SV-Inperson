class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        post = 0
        neg = 0
        for num in nums:
            if num < 0:
                neg += 1
            elif num > 0:
                post += 1
        return max(post, neg)
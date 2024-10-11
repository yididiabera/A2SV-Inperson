class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        count = 0

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                count += 1
        
        if (count == 0) or (count == 1 and nums[0] >= nums[n - 1]):
            return True
        
        return False
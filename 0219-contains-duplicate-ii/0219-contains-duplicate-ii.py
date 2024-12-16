class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0 or not nums:
            return False
        
        window = {}
        k = min(k, len(nums))  # Ensure k is within nums length

        for i in range(k):
            if nums[i] in window:
                return True
            window[nums[i]] = window.get(nums[i], 0) + 1
        
        for i in range(k, len(nums)):
            if nums[i] in window:
                return True
            window[nums[i]] = window.get(nums[i], 0) + 1
            window[nums[i - k]] -= 1
            if window[nums[i - k]] == 0:
                del window[nums[i - k]]
        
        return False

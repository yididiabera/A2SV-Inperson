class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        windows = set()
        l = 0

        for r in range(len(nums)):
            if nums[r] in windows:
                return True
            windows.add(nums[r])

            if r - l + 1 > k:
                windows.remove(nums[l])
                l += 1
        return False
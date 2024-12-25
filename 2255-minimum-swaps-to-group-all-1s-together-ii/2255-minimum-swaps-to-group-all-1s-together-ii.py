class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        k = nums.count(1)
        _max  = 0
        cur = 0
        l = 0
        for r in range(2 * N):
            if nums[r % N] == 1:
                cur += 1
            if r - l + 1 > k:
                cur -= nums[l % N]
                l += 1
            _max = max(_max, cur)
        return k - _max
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        _max = 1
        i_count = 1
        d_count = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                i_count += 1
                d_count = 1
                _max = max(_max, i_count)
            elif nums[i] > nums[i + 1]:
                d_count += 1
                i_count = 1
                _max = max(_max, d_count)
            else:
                i_count = 1
                d_count = 1
        return _max
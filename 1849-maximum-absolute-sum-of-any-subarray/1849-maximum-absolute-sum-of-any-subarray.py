class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = min_sum = 0
        max_ending_here = min_ending_here = 0

        for num in nums:
            max_ending_here = max(num, max_ending_here + num)
            min_ending_here = min(num, min_ending_here + num)

            max_sum = max(max_sum, max_ending_here)
            min_sum = min(min_sum, min_ending_here)

        return max(max_sum, abs(min_sum))
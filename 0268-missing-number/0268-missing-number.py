class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expectedSum = n * (n + 1) // 2
        sum_of_nums = sum(nums)

        return expectedSum - sum_of_nums

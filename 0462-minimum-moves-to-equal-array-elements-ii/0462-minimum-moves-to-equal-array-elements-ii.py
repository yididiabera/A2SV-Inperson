class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        med = n // 2
        pivot = nums[med]
        result = 0

        for num in nums:
            result += abs(pivot - num)
        return result 
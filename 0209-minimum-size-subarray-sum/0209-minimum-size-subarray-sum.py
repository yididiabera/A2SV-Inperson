class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total, l = 0, 0
        result = len(nums) + 1

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                result = min(result, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if result > len(nums) else result
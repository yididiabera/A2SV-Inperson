class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        result = 0
        MOD = 10**9 + 7
        prefix = [0] * (n + 1)
        
        for start, end in requests:
            prefix[start] += 1
            prefix[end + 1] -= 1

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + prefix[i]
        # if len(prefix) > len(nums):
        prefix.pop()
        prefix.sort()
        nums.sort()
        
        for i in range(len(nums)):
            result += nums[i] * prefix[i]
        return result % MOD
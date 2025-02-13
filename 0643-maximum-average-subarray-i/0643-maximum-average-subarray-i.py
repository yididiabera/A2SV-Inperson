class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        _sum = 0
        n = len(nums)
        for i in range(k):
            _sum += nums[i]
        
        _max = _sum
        for i in range(k, n):
            _sum -= nums[i - k]
            _sum += nums[i]
            _max = max(_max, _sum)
        return _max / k

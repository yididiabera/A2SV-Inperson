class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = {}
        good_pair = 0
        n = len(nums)
        total_pair = n * (n - 1) // 2
        for idx, num in enumerate(nums):
            key = idx - num
            good_pair += count.get(key, 0)
            count[key] = count.get(key, 0) + 1
        
        return total_pair - good_pair
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        _min = float("inf")

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                _min = min(_min, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if _min == float("inf") else _min
       
       
        # l = 0
        # _min = len(nums) + 1 
        # total = 0

        # for r in range(len(nums)):
        #     total += nums[r]
        #     while total >= target:
        #         _min = min(_min, r - l + 1)
        #         total -=  nums[l]
        #         l += 1
        # return 0 if _min > len(nums) else _min
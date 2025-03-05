class Solution:
    def canJump(self, nums: List[int]) -> bool:
        _max = 0
        for i in range(len(nums)):
            if i > _max:
                return False
            _max = max(_max, nums[i] + i)
        return True
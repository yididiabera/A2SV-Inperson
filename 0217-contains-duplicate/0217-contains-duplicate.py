class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = Counter(nums)
        for i in nums:
            if hash_map[i] > 1:
                return True
        return False
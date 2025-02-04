class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = Counter(nums)
        n = len(nums)
        print(hash_map)
        for num in nums:
            if hash_map[num] > (n // 2):
                return num
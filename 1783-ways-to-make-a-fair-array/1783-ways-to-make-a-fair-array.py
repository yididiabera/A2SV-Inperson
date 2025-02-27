class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        even_prefix, odd_prefix = 0, 0
        even_total, odd_total = 0, 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                even_total += num
            else:
                odd_total += num

        count = 0  # Number of indices that make the array fair
        
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even_new = even_prefix + (odd_total - odd_prefix)
                odd_new = odd_prefix + (even_total - even_prefix - num)
            else:
                even_new = even_prefix + (odd_total - odd_prefix - num)
                odd_new = odd_prefix + (even_total - even_prefix)

            if even_new == odd_new:
                count += 1

            if i % 2 == 0:
                even_prefix += num
            else:
                odd_prefix += num
        
        return count

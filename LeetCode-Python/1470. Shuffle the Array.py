class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        l, r = 0, n
        result = []
        for _ in range(n):
            result.append(nums[l])
            result.append(nums[r])
            l, r = l + 1, r + 1
        return result
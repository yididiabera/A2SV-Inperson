class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for n in nums:
            n = abs(n)
            if nums[n - 1] < 0:
                result.append(n)
            nums[n - 1] = -nums[n - 1]
        return result

        # freq = {}
        # result = []
        # n = len(nums)
        # for i in range(n):
        #     freq[nums[i]] = freq.get(nums[i], 0) + 1
        # for n in freq:
        #     if freq[n] == 2:
        #         result.append(n)
        # return result
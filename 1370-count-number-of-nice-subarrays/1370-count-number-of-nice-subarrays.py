class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix = { 0: 1}
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        _sum = 0
        for i in range(len(nums)):
            _sum +=  nums[i]
            dif = _sum - k
            count += prefix.get(dif, 0)
            prefix[_sum] = prefix.get(_sum, 0) + 1
        return count
        # count = 0
        # for i in range(len(nums)):
        #     oddCount = 0
        #     for j in range(i, len(nums)):
        #         if nums[j] % 2 == 1:
        #             oddCount += 1
        #         if oddCount == k:
        #             count += 1
        # return count
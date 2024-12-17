class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        curSum = 0
        prefix = {0:1}
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                curSum += 1
            
            if curSum - k in prefix:
                count += prefix[curSum - k]
            prefix[curSum] = prefix.get(curSum, 0) + 1
        return count

        # result = 0
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(i, len(nums)):
        #         if nums[j] % 2 == 1:
        #             count += 1
        #         if count == k:
        #             result += 1
        # return result
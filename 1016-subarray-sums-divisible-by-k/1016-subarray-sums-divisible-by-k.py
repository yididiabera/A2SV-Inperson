class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        rem_count = {0:1}
        count = 0
        prefix = 0

        for num in nums:
            prefix += num
            rem = prefix % k
            if rem < 0:
                rem = rem + k
            
            if rem in rem_count:
                count += rem_count[rem]
            rem_count[rem] = rem_count.get(rem, 0) + 1
        return count
        

        # count = 0
        # for i in range(len(nums)):
        #     _sum = 0
        #     for j in range(i, len(nums)):
        #         _sum += nums[j]
        #         if _sum % k == 0:
        #             count += 1
        # return count

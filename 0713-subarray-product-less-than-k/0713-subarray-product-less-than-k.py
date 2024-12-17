class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        product = 1
        count = 0
        l = 0
        for r in range(len(nums)):
            product *= nums[r]
            while product >= k and l <= r:
                product = product // nums[l]
                l += 1
            count += (r - l + 1)
        return count

        # remCount = {0:1}
        # prefix = 1
        # count = 0
        # for i in range(len(nums)):
        #     prefix *= nums[i]
        #     rem = prefix % k

        #     if:
        #         pass
        #     remCount[rem] = remCount.get(rem, 0) + 1
        # return count           
    
        # count = 0
        # for i in range(len(nums)):
        #     _product = 1
        #     for j in range(i, len(nums)):
        #         _product *= nums[j]
        #         if _product < k:
        #             count += 1
        # return count
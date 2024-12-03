class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #iterate over the entire array
        #check if the current element and the previous one are equal or not
        #if they are equal mulitply the prev element by 2 and make the current zero
        n = len(nums)
        l = 0
        for r in range(n):
            if r < n - 1 and nums[r] == nums[r + 1]:
                nums[r] *= 2
                nums[r + 1] = 0
            if nums[r]:
                nums[l] = nums[r]
                if l != r:
                    nums[r] = 0
                l += 1
        return nums
        
        
        # n = len(nums)
        # l = 0
        # for r in range(len(nums)):
        #     if r < n - 1 and nums[r] == nums[r + 1]:
        #         nums[r] *= 2
        #         nums[r + 1] = 0
            
        #     if nums[r]:
        #         nums[l] = nums[r]
        #         if l != r:
        #             nums[r] = 0
        #         l += 1
        # return nums
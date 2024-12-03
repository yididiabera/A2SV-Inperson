class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #iterate over the entire array
        #check if the current element and the previous one are equal or not
        #if they are equal mulitply the prev element by 2 and make the current zero
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # compute the total sum and initialize leftSum = 0
        #iterate over the entire array and calcuate the leftSum by adding the values
        #and compute the rightSum by subtracting the leftSum and the current index element
        #if the leftSum and rightSum are equal then return the index
        total = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]

        return -1
        
        # for i in range(len(nums)):
        #     prefixSum = sum(nums[:i])
        #     postfixSum = sum(nums[i + 1:])
            
        #     if prefixSum == postfixSum:
        #         return i
        # return -1

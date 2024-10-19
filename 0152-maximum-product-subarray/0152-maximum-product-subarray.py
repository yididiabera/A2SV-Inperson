class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = maxProduct = nums[0]

        for n in nums[1:]:
            if n < 0:
                curMax, curMin = curMin, curMax
            
            curMax = max(n, curMax * n)
            curMin = min(n, curMin * n)
            maxProduct = max(curMax, maxProduct)
        return maxProduct
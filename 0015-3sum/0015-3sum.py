class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []

        for i, value in enumerate(nums):
            if i > 0 and nums[i - 1] == value:
                continue
            
            l, r = i + 1, len(nums) - 1
            while(l < r):
                threeSum = value + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else: 
                    result.append([value, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result
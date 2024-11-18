class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        return nums[k -1]

        # n = len(nums)
        # nums.sort()
        # return nums[n - k]

        # k = len(nums) - k
        # def quickSelect(l, r):
        #     p, pivot = l, nums[r]

        #     for i in range(l, r):
        #         if nums[i] <= pivot:
        #             nums[i], nums[p] = nums[p], nums[i]
        #             p += 1
        #     nums[p], nums[r] = nums[r], nums[p]

        #     if p < k:
        #         return quickSelect(p + 1, r)
        #     elif p > k:
        #         return quickSelect(l, p - 1)
        #     else: 
        #         return nums[p]
        
        # return quickSelect(0, len(nums) - 1)

        # for i in range(n - 1):  -- O(n^2)
        #     for j in range(n - 1 - i):
        #         if nums[j] < nums[j + 1]:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
        # return nums[k - 1]
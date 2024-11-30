class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #reverse the whole array
        #reverse again upto k
        #reverse from k up to the end of the array
        n = len(nums)
        k %= n
        l, r = 0, len(nums) - 1
        def reverseArray(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
        reverseArray(l, r)
        reverseArray(0, k - 1)
        reverseArray(k, n - 1)



        # n = len(nums)
        # temp = [0] * n
        # k %= n
        # for i in range(n):
        #     temp[(i + k) % n] = nums[i]
        # for i in range(n):
        #     nums[i] = temp[i]
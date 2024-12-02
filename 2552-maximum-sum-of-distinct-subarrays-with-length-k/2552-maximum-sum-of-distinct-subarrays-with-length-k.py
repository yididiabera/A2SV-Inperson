class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #create a window set to check if the elements are duplicate and
        #curSum vairable to hold the current sum
        #remove the leftmost elements if they the size of the window exceeds k
        window = {}
        _max = 0
        curSum = 0
        l = 0
        for r in range(len(nums)):
            window[nums[r]] = window.get(nums[r], 0) + 1
            curSum += nums[r]

            if r - l + 1 > k:
                window[nums[l]] -= 1
                if window[nums[l]] == 0:
                    del window[nums[l]]
                curSum -= nums[l]
                l += 1
            
            if r - l + 1 == k and len(window) == k:
                _max = max(_max, curSum)
        return _max

        # #intialize a sliding window with size k
        # #ieterate through the nums and check if they meet the coditions 
        # #if so find the sum
        # _max = 0
        # _sum = 0
        # window = nums[:k - 1]

        # for i in range(k - 1, len(nums)):
        #     window.append(nums[i])
        #     checker = collections.Counter(window) # not efficient for large inputs because it uses O(k) - the O(n * k)
        #     if len(checker) == k:
        #         _sum = sum(window)
        #     _max = max(_max, _sum)

        #     del window[0]
        # return _max 
            
            
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum = 0
        count = 0
        prefixSums = {0 : 1}

        for num in nums:
            curSum += num
            dif = curSum - k
            count += prefixSums.get(dif, 0)
            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1
        return count
        
        # l = 0
        # count = 0
        # window = 0

        # for i in range(len(nums)):
        #     window += nums[i]

        #     while window > k:
        #         window -= nums[l]
        #         l += 1
                
        #     if window == k:
        #         count += 1

            

        # return count
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        curSum = 0
        prefixSum = {0:1}

        for n in nums:
            curSum += n
            dif = curSum - k

            result += prefixSum.get(dif, 0)
            prefixSum[curSum] = prefixSum.get(curSum, 0) + 1
        return result
        
        
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
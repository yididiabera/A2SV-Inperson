class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #iterate through the number and calculate the running sum
        #check if the curSum - k equals to the prev subarray
        #if so there exists a sum of k between the pt and the current index
        #use hashmap to hold the frequency of the prefix sum
        prefix = {0:1}
        count = 0
        _sum = 0

        for i in range(len(nums)):
            _sum += nums[i]
            dif = _sum - k
            if dif in prefix:
                count += prefix[dif]
            prefix[_sum] = prefix.get(_sum, 0) + 1
        return count
        # curSum = 0
        # count = 0
        # prefixSums = {0 : 1}

        # for num in nums:
        #     curSum += num
        #     dif = curSum - k
        #     count += prefixSums.get(dif, 0)
        #     prefixSums[curSum] = prefixSums.get(curSum, 0) + 1
        # return count
        
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
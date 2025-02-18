class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        _sum = 0
        result = []
        count = 0
        sum_count = { 0:1 }
        for num in nums:
            _sum += num
            dif = _sum - goal
            if dif in sum_count:
                count += sum_count[dif]
            sum_count[_sum] = sum_count.get(_sum, 0) + 1
        return count
        # for num in nums:
        #     _sum += num
        #     result.append(_sum)
        
        # for n in result:
        #     dif = n - goal
        #     if dif in sum_count:
        #         count += sum_count[dif]
        #     sum_count[dif] = sum_count.get(dif, 0) + 1
        # return count
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # (1,2) (3,3) (5, 1) (2,14)
        sorted_nums = sorted(zip(nums, cost))
        costs = sum(cost)
        result = 0
        prefix = [0] * len(cost)

        for i in range(len(sorted_nums)):
            prefix[i] = (prefix[i - 1] if i > 0 else 0) + sorted_nums[i][1]
        
        med_idx = 0
        for idx, num in enumerate(prefix):
            if num >= (costs / 2):
                med_idx = idx
                break
        pivot = sorted_nums[med_idx][0]

        for num, costt in zip(nums, cost):
            result += (abs(pivot - num)) * costt
        
        return result
        
        
        # med = float("inf")
        # med_idx = 0
        # for idx, val in enumerate(prefix):
        #     med = min(med, abs(val - costs // 2))
        #     if med == abs(val - (costs // 2)):
        #         med_idx = idx
        # pivot = sorted_nums[med_idx][0]
        
        # for num, idx in sorted_nums:
        #     result += (abs(pivot - num) * idx)
        
        # for i in range(len(nums)):
        #     result += abs(nums[i] - pivot) * cost[i]
        
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        heapq.heapify(nums)

        while len(nums) > 1:
            a , b = heapq.heappop(nums) , heapq.heappop(nums)
            if a >=k and b>=k:
                return ans
            ans += 1
            heapq.heappush(nums , min(a , b) * 2 + max(a , b))
        return ans
            


        return ans
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        temp = nums[:]
        _sum = sum(num for num in nums if num % 2 == 0)
        
        for val, idx in queries:
            t = temp[idx] + val
           
            if temp[idx] % 2 == 0:
                if t % 2 == 1:
                    _sum -= temp[idx]
                else:
                    _sum -= temp[idx]
                    _sum += t
            else:
                if t % 2 == 0:
                    _sum += t
            temp[idx] = t
            result.append(_sum)
        return result

        # def even(arr):
        #     even = [0] * (len(arr))
        #     for idx, val in enumerate(arr):
        #         if val % 2 == 0:
        #             even[idx] = val
        #         even_sum = sum(even)
        #     return even_sum
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def can_zero_out(k):
            """Check if first k queries can zero out the array."""
            diff = [0] * (len(nums) + 1)
            arr = nums[:]  # Copy of nums
            
            for i in range(k):
                l, r, v = queries[i]
                diff[l] -= v
                if r + 1 < len(nums):
                    diff[r + 1] += v
            
            curr = 0
            for i in range(len(nums)):
                curr += diff[i]
                arr[i] += curr  # Apply the difference array
                
                if arr[i] > 0:
                    return False  # If any element remains > 0, return False
            
            return True  # If all elements are zero or less, return True
        
        # Binary search on the number of queries needed
        left, right = 0, len(queries)  # Start at 0 to check for initial zero case
        answer = -1
        
        while left <= right:
            mid = (left + right) // 2
            if can_zero_out(mid):
                answer = mid
                right = mid - 1  # Try fewer queries
            else:
                left = mid + 1  # Try more queries
        
        return answer

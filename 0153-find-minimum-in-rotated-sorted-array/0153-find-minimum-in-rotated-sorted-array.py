from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If mid element is greater than rightmost element, pivot is on the right side
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid  # Include mid because it could be the min
                
        return nums[left]  # At the end, left == right

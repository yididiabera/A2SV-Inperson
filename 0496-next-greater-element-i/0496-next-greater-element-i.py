class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1 = [4, 1, 2]   nums2 = [1, 3, 4, 2]
        n = len(nums1)
        m = len(nums2)
        result = [-1] * n
        
        for i in range(n):
            found = False
            for j in range(m):
                if nums1[i] == nums2[j]:
                    found = True
                if found and nums2[j] > nums1[i]:
                    result[i] = nums2[j]
                    break
        return result
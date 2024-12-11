class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1 = [4, 1, 2]   nums2 = [1, 3, 4, 2]
        n = len(nums1)
        m = len(nums2)
        result = []
        for i in range(n):
            found = False
            for j in range(m):
                if nums1[i] == nums2[j]:
                    index = j
                    while index < m:
                        if nums2[index] > nums1[i]:
                            result.append(nums2[index])
                            found = True
                            break
                        index += 1
                        
                    if not found:
                        result.append(-1)
                    # break
        return result
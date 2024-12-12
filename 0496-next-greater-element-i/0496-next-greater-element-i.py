class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1Idx = {}
        for i, value in enumerate(nums1):
            nums1Idx[value] = i
        
        result = [-1] * len(nums1)
        m = len(nums2)
        for i in range(m):
            if nums2[i] not in nums1Idx:
                continue
            for j in range(i + 1, m):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    result[idx] = nums2[j]
                    break
        return result
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)
       
        _max = -1
        for i in range(n):
            _max = max(_max, nums1[i][0])
        for i in range(m):
            _max = max(_max, nums2[i][0])
        result = [[0, 0] for _ in range(_max + 1)]
        
        i = j = 0

        while i < n and j < m:
            if nums1[i][0] == nums2[j][0]:
                result[nums1[i][0]] = [nums1[i][0], nums1[i][1] + nums2[j][1]]
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                result[nums1[i][0]] = [nums1[i][0], nums1[i][1]]
                i += 1
            elif nums1[i][0] > nums2[j][0]:
                result[nums2[j][0]] = [nums2[j][0], nums2[j][1]]
                j += 1
        while i < n:
            result[nums1[i][0]] = [nums1[i][0], nums1[i][1]]
            i += 1

        while j < m:
            result[nums2[j][0]] = [nums2[j][0], nums2[j][1]]
            j += 1
        return [pair for pair in result if pair != [0, 0]]

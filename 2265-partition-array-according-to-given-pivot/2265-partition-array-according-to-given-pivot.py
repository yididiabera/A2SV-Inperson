class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # elements < pivot --> before other elements
        # elements == pivot --> between 
        # relative order is maintained
        small = []
        eq = []
        large = []

        for num in nums:
            if num < pivot:
                small.append(num)
            elif num == pivot:
                eq.append(num)
            else:
                large.append(num)
        return small + eq + large
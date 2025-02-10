class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count1 = Counter(arr1)
        result = []
        for num in arr2:
            for _ in range(count1[num]):
                result.append(num)
        left_over = []
        for num in arr1:
            if num not in arr2:
                left_over.append(num)
        left_over.sort()
        for num in left_over:
            result.append(num)
        
        return result
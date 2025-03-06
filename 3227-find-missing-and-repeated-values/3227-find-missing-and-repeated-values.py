class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_elements = n * n

        count = [0] * (total_elements + 1)
        
        for row in grid:
            for num in row:
                count[num] += 1
        
        a, b = -1, -1
        for num in range(1, total_elements + 1):
            if count[num] == 2:  # Repeated number
                a = num
            elif count[num] == 0:  # Missing number
                b = num

        return [a, b]

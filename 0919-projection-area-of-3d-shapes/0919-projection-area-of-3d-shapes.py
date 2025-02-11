class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        top = 0
        right = 0
        front = 0
        front_max = [0] * n
        
        for i in range(n):
            right_max = 0
            for j in range(m):
                val = grid[i][j]
                if val != 0:
                    top += 1
                right_max = max(right_max, val)
                front_max[j] = max(front_max[j], val)
            right += right_max
        total = top + right + sum(front_max)
        return total 
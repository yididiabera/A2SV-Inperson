class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        N = len(grid)
        maxLocal = [[0] * (N - 2) for _ in range(N - 2)]

        for i in range(N - 2):
            for j in range(N - 2):
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        maxLocal[i][j] = max(maxLocal[i][j], grid[r][c])
        return maxLocal
    
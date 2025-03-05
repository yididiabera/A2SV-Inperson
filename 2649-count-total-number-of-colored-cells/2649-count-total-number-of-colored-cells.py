class Solution:
    def coloredCells(self, n: int) -> int:
        colored = 2 * (n * ( n - 1))
        return colored + 1

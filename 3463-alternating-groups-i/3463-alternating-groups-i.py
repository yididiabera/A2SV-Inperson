class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count = 0
        n = len(colors)
        i = 0
        while i < n:
            idx_left = (i - 1) % n
            idx_right = (i + 1) % n
            if colors[idx_left] == colors[idx_right] and colors[idx_left] != colors[i]:
                count += 1
            i += 1
        
        return count
        

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        left = 0
        count = 0
        for right in range(1, n + k - 1):
            if colors[right % n] == colors[(right - 1) % n]:
                left = right
            
            if right - left + 1 > k:
                left += 1
            
            if right - left + 1 == k:
                count += 1
        return count
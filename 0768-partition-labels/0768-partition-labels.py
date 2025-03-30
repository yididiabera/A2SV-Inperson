class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        result = []
        size = 0
        end = 0
        for i,c in enumerate(s):
            end = max(end, lastIndex[c])
            size += 1
            if i == end:
                result.append(size)
                size = 0
        return result
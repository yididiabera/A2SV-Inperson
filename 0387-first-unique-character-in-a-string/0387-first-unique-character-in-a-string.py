class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        for c in s:
            hash_map[c] = hash_map.get(c, 0) + 1
    
        for i in range(len(s)):
            if hash_map[s[i]] == 1:
                return i
        return -1
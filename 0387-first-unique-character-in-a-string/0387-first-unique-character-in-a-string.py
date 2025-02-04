class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        for ch in s:
            hash_map[ch] = hash_map.get(ch, 0) + 1
        for idx, value in enumerate(s):
            if hash_map[value] == 1:
                return idx
        return -1
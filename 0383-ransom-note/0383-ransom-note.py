class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countM = {}
        countR = {}
        for c in magazine:
            countM[c] = countM.get(c, 0) + 1
        for c in ransomNote:
            countR[c] = countR.get(c, 0) + 1
        
        for c in ransomNote:
            if countR[c] > countM.get(c, 0):
                return False
        return True
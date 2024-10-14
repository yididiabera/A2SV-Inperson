class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        target, window = {}, {}
        k = len(p)

        for c in p:
            if c not in target:
                target[c] = 1
            else:
                target[c] += 1
        
        for i in range(len(s)):
            if s[i] not in window:
                window[s[i]] = 1
            else:
                window[s[i]] += 1
            
            if i >= k:
                left_char = s[i - k]
                if window[left_char] == 1:
                    del window[left_char]
                else:
                    window[left_char] -= 1
            
            if window == target:
                result.append(i - k + 1)
        return result
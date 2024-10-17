class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)

        s1_count = Counter(s1)
        window_count = Counter(s2[:k])

        if s1_count == window_count:
            return True
        
        for i in range(k, n):
            window_count[s2[i]] += 1
            window_count[s2[i - k]] -= 1
            
            # if window_count[s2[i - k]] == 0:
            #     del window_count[s2[i - k]]
            
            if s1_count == window_count:
                return True
        
        return False
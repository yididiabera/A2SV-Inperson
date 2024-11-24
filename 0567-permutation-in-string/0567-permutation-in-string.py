class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)

        target = Counter(s1)
        window = Counter(s2[:k - 1])

        for i in range(k - 1, n):
            window[s2[i]] += 1

            if target == window:
                return True
            
            window[s2[i - k + 1]] -= 1
        return False
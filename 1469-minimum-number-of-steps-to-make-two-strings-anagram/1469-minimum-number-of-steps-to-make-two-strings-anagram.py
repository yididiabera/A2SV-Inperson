class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        count = 0

        for ch in s_count:
            if t_count[ch] < s_count[ch]:
                count += s_count[ch] - t_count[ch]
        return count
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        _max = 0
        count = Counter()

        for r in range(len(s)):
            count[s[r]] += 1

            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            _max = max(_max, r - l + 1)
        return _max
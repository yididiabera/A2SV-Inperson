class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        l = 0
        _max = 0

        for r in range(len(s)):
            cur = s[r]
            # window[cur] += 1
            window[cur] = window.get(cur, 0) + 1
            while window[cur] > 1:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1

            _max = max(_max, r - l + 1)
        return _max
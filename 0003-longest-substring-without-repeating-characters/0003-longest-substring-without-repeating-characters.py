class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = collections.Counter()
        l = 0
        _max = 0

        for r in range(len(s)):
            window[s[r]] += 1

            while window[s[r]] > 1:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            _max = max(_max, r - l + 1)
        return _max
class Solution(object):
    def longestContinuousSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 1
        _max = 1

        for i in range(1, len(s)):
            if ord(s[i - 1]) + 1 == ord(s[i]):
                count += 1
                _max = max(_max, count)
            else:
                count = 1
        return _max
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        k = 3
        for i in range(len(s) - k + 1):
            window = s[i: i + k]
            if len(set(window)) == k:
                count += 1
        return count
        # count = 0
        # windows = {}
        # l = 0
        # k = 3

        # for r in range(len(s)):
        #     if s[r] not in windows:
        #         windows[s[r]] = 1
        #     else:
        #         windows[s[r]] += 1
            
        #     if r - l + 1 > k:
        #         left = s[l]
        #         if windows[left] == 1:
        #             del windows[left]
        #         else:
        #             windows[left] -= 1
        #         l += 1
        #     if len(windows) == k:
        #         count += 1
        # return count
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def checker():
            for ch in count:
                if window[ch] < count[ch]:
                    return False
            return True
        l = 0

        #_min = float("inf")
        count = Counter(t)
        window = defaultdict(int)
        ans = [float("-inf"), float("inf")]

        for r in range(len(s)):
            window[s[r]] += 1

            while checker():
                if r - l < ans[1] - ans[0]:
                    ans = [l, r]
                #_min = min(_min, r - l + 1)
                window[s[l]] -= 1
                # if window[s[l]] == 0:
                #     del window[s[l]]
                l += 1
        if ans == [float("-inf"), float("inf")]:
            return ""
        else:
            return s[ans[0] : ans[1] + 1]


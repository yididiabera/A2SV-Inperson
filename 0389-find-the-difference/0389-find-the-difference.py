class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sHash = Counter(s)
        for c in t:
            if sHash[c] == 0:
                return c
            sHash[c] -= 1

        # sHash = {}
        # tHash = {}

        # for c in s:
        #     sHash[c] = sHash.get(c, 0) + 1
        # for c in t:
        #     tHash[c] = tHash.get(c, 0) + 1
        # for c in t:
        #     if c not in sHash or tHash[c] > sHash[c]:
        #         return c

            
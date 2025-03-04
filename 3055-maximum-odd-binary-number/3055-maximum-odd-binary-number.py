class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = Counter(s)

        return "".join(['1'] * (count['1'] - 1) + ['0'] * count['0'] + ['1'] )
        # s_reversed= sorted(s, reverse=True)
        # count = 0
        # for ch in s_reversed:
        #     if ch == '1':
        #         count += 1
        # if count < 1:
        #     s.sort()
        #     return "".join(s)
        # else:
        #     for i in range(len(s) - 1, -1, -1):
        #         if s_reversed[i] == '1':
        #             s_reversed[i], s_reversed[-1] = s_reversed[-1], s_reversed[i]
        #             break
        # return "".join(s_reversed)



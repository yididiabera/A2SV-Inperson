class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        s = list(s)
        n = len(shifts)
        dif = [0] * n
        _sum = sum(shifts)
        for i in range(n):
            dif[i] = _sum
            s[i] = chr((ord(s[i]) - ord('a') + dif[i]) % 26 + ord('a'))
            _sum = _sum - shifts[i]
        return "".join(s)
        #time limit exceeded
        # s = list(s)
        # for i in range(len(shifts)):
        #     for j in range(i + 1):
        #         s[j] = chr(((ord(s[j]) - ord('a') + shifts[i]) % 26) + ord('a'))
        #     print(s)
        # return "".join(s)
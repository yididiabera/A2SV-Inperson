class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        #create a dif array - with +1 size to hold the amount of shifts on each char
        # +1 because as a flag to know where the shifting ends
        #calculate the prefix sum of the dif
        #and shift the string accordingly

        s = list(s)
        n = len(s)
        dif = [0] * (n + 1)
        for start, end, direction in shifts:
            if direction == 1:
                dif[start] += 1
                dif[end + 1] -= 1
            else:
                dif[start] -= 1
                dif[end + 1] += 1
        
        for i in range(1, len(dif)):
            dif[i] = dif[i - 1] + dif[i]
        
        for i in range(n):
            s[i] = chr((ord(s[i]) - ord('a') + dif[i]) % 26 + ord('a'))
        return ''.join(s)

        # s = list(s)
        # for start, end, direction in shifts:
        #     for i in range(start, end + 1):
        #         if direction == 1:
        #             s[i] = chr(((ord(s[i]) - ord('a') + 1) % 26) + ord('a'))
        #         else:
        #             s[i] = chr(((ord(s[i]) - ord('a') - 1) % 26) + ord('a'))
        # return "".join(s)
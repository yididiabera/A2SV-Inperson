class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        count = 0
        num_str = str(num)

        for i in range(len(num_str) - k + 1):
            window = num_str[i: i + k]

            if int(window) != 0 and num % int(window) == 0:
                count += 1
        return count 

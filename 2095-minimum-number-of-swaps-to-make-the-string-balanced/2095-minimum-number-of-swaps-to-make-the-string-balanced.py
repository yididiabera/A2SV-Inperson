class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        balance = 0
        max_imbalance = 0

        for char in s:
            if char == '[':
                balance += 1
            else:
                balance -= 1

            # Track the maximum imbalance
            max_imbalance = min(max_imbalance, balance)

        # Number of swaps needed is the absolute value of max imbalance
        return (-max_imbalance + 1) // 2
class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = []
        if num % 3 != 0:
            return result
        x = num / 3
        return [x - 1, x, x + 1]
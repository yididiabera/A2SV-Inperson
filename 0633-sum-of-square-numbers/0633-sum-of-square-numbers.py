class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        #start with two pointers: one at zero and the other one the square root of the target no-c
        #iterate until the two poiters are equal and calculate the sum of the square of each pointers and shift the pointers accordingly
        #if it is equal to the number, return True and false otherwise

        l, r = 0, int(c ** 0.5)
        while l <= r:
            cur_sum = l * l + r * r
            if cur_sum == c:
                return True
            elif cur_sum < c:
                l += 1
            else:
                r -= 1
        return False
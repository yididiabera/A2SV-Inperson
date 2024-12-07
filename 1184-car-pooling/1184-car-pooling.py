class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        total = [0] * 1001
        for passenger, start, end in trips:
            for i in range(start, end):
                total[i] += passenger
                if total[i] > capacity:
                    return False
        return True


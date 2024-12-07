class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        dif = [0] * 1001

        for passenger, start, end in trips:
            dif[start] += passenger
            dif[end] -= passenger
        
        curPassenger = 0
        for passenger in dif:
            curPassenger += passenger
            if curPassenger > capacity:
                return False
        return True

        
        # total = [0] * 1001
        # for passenger, start, end in trips:
        #     for i in range(start, end):
        #         total[i] += passenger
        #         if total[i] > capacity:
        #             return False
        # return True


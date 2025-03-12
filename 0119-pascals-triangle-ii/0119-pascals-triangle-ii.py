class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [[1]]
        
        for i in range(1, rowIndex + 1):
            temp = [0] + result[-1] + [0]
            new_row = [0] * (len(result[-1]) + 1)

            for j in range(len(new_row)):
                new_row[j] = temp[j] + temp[j + 1]
            result.append(new_row)

        return result[-1]

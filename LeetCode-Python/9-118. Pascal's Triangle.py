class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1]]

        for i in range(1, numRows):
            aRow = [1]
            for j in range(1, i):
                element = result[i - 1][j - 1] + result[i - 1][j]
                aRow.append(element)
            aRow.append(1)
            result.append(aRow)
        return result
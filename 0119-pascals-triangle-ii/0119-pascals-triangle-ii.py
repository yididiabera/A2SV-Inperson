class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]
        temp = [0]
        for i in range(rowIndex):
            temp = [0] * (len(result) + 1)
            for j in range(len(result)):
                temp[j] += result[j]
                temp[j + 1] += result[j]
            result = temp
        return result
        
            
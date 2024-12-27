class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        #iterate through the matrix starting from the row idx 1 and column idx 1
        #check whether the element is equal to element found idx - 1 (top left element)
        prev_row = None
        for cur_row in matrix:
            if prev_row:
                for j in range(1, len(cur_row)):
                    if cur_row[j] != prev_row[j - 1]:
                        return False
            prev_row = cur_row
        return True



        # for i in range(1, len(matrix)):
        #     for j in range(1, len(matrix[i])):
        #         if matrix[i][j] != matrix[i - 1][j - 1]:
        #             return False
        # return True
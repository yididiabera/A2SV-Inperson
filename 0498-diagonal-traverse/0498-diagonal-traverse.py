class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        dick = {}
        res = []
        for i in range(rows):
            for j in range(cols):
                value = mat[i][j]
                if i + j not in dick:
                    dick[i + j] = [value]
                else:
                    dick[i + j].append(value)
        for key, value in dick.items():
            if key % 2 == 0:
                value.reverse()
                res.append(value)
            else:
                res.append(value)
        
        ans = []
        for i in range(len(res)):
            for j in range(len(res[i])):
                ans.append(res[i][j])
        return ans



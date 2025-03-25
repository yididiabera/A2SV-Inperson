class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = []

        def backtrack(i, path):
            if len(path) == n:
                result.append("".join(path))
                return 
            
            path.append("1")
            backtrack(i + 1, path)
            path.pop()

            if not path or path[-1] == "1":
                path.append("0")
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return result
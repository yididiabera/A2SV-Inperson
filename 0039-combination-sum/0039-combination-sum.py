class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def backtrack(i, path, total):
            if total == target:
                answer.append(path[:])
                return
            
            if i >= len(candidates) or total > target:
                return 
            
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])
            path.pop()

            backtrack(i + 1, path, total)

        backtrack(0, [], 0)
        return answer
        
        # candidates.sort()
        # answer = []

        # def backtrack(i, path):
        #     if sum(path) == target:
        #         answer.append(path[:])
            
        #     if i > len(candidates):
        #         return
            
        #     path.append(i)
        #     backtrack(i + 1, path)
        #     path.pop()

        #     backtrack(i + 1, path)
        
        # backtrack(1, [])
        # return answer
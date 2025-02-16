class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = 2 * n - 1
        res = [0] * size
        used = set()  # To track numbers used in the sequence

        def backtrack(index: int) -> bool:
            if index == size:  # If we've filled the sequence
                return True
            
            if res[index] != 0:  # Skip if the position is already occupied
                return backtrack(index + 1)

            for num in range(n, 0, -1):  # Start placing from the largest number
                if num in used:
                    continue
                
                if num == 1:
                    res[index] = 1
                    used.add(1)
                    if backtrack(index + 1):
                        return True
                    res[index] = 0
                    used.remove(1)
                else:
                    second_index = index + num
                    if second_index < size and res[second_index] == 0:
                        res[index], res[second_index] = num, num
                        used.add(num)
                        if backtrack(index + 1):
                            return True
                        res[index], res[second_index] = 0, 0
                        used.remove(num)
            
            return False

        backtrack(0)
        return res

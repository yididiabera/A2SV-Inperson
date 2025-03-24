class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
            
        hashmap = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
        }
        result = [""]

        for digit in digits:

            temp = []
            for pre in result:
                for ch in hashmap[digit]:
                    temp.append(pre + ch)
            result = temp
        
        return result
        
            

        # for i in range(len(digits)):
        #     key = 
        #     for j in range(i + 1, len(digits)):
        #         key = digits[i]
        #         result.append(hashmap[key][j])
        
        # return result        
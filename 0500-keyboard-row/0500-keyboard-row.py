class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        def is_one_row(word):
            lower_word = set(word.lower())  
            return lower_word <= row1 or lower_word <= row2 or lower_word <= row3  
        
        return [word for word in words if is_one_row(word)]

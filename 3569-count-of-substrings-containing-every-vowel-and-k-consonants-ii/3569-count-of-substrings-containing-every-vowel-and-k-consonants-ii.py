class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atleastk(k):
            vowel = defaultdict(int)
            result = 0
            consonants = 0
            l = 0
        
            for r in range(len(word)):
                if word[r] in "aeiou":
                    vowel[word[r]] += 1
                else:
                    consonants += 1
                
                while len(vowel) == 5 and consonants >= k:
                    result += len(word) - r
                    if word[l] in "aeiou":
                        vowel[word[l]] -= 1
                        if vowel[word[l]] == 0:
                            del vowel[word[l]]
                    else:
                        consonants -= 1
                    l += 1

            return result
        return atleastk(k) - atleastk(k + 1)
                            

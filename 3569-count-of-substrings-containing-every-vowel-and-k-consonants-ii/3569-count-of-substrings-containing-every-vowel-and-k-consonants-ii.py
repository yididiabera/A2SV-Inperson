class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atleastk(k):
            vowel = defaultdict(int)
            consonants = 0
            l = 0
            count = 0
            
            for i in range(len(word)):
                if word[i] in "aeiou":
                    vowel[word[i]] += 1
                else:
                    consonants += 1
            
                while len(vowel) == 5 and consonants >= k:
                    count += len(word) - i
                    if word[l] in "aeiou":
                        vowel[word[l]] -= 1
                        if vowel[word[l]] == 0:
                            del vowel[word[l]]
                    else:
                        consonants -= 1
                    l += 1
            return count   

        return atleastk(k) - atleastk(k + 1)
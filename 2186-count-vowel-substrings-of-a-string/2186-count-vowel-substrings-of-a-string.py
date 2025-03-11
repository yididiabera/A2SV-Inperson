class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        j = k = 0
        count = 0
        vowel = defaultdict(int)
        unique_vowel = 0

        for i in range(len(word)):
            if word[i] in "aeiou":
                vowel[word[i]] += 1
                # if vowel[word[i]] == 1:
                #     unique_vowel += 1

                while len(vowel) == 5:
                    vowel[word[k]] -= 1
                    if vowel[word[k]] == 0:
                        del vowel[word[k]]
                    k += 1
                count += k - j
    
            else: # if the character is a constant
                j = k = i + 1
                vowel.clear()
                unique_vowel = 0
        return count
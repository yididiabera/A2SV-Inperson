class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(word: str) -> bool:
            l, r = 0, len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        for word in words:
            if isPalindrome(word):
                return word
        return ""
        # for word in words:
        #     is_palindrome = True
        #     l, r = 0, len(word) - 1
        #     while l < r:
        #         if word[l] != word[r]:
        #             is_palindrome = False
        #             break
        #         l += 1
        #         r -= 1
            
        #     if is_palindrome:
        #         return word
        # return ""
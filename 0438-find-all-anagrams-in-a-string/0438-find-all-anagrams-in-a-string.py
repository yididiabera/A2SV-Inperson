class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        target_counts = Counter(p)
        window_counts = Counter(s[:len(p)])  # Initialize window with the first l  (p) characters

        # Start checking from index len(p) to len(s)
        for i in range(len(p), len(s)):
            # Check if the current window matches the target
            if window_counts == target_counts:
                result.append(i - len(p))
            
            # Slide the window by removing the leftmost character and adding the new character
            window_counts[s[i]] += 1
            window_counts[s[i - len(p)]] -= 1
            
            if window_counts[s[i - len(p)]] == 0:
                del window_counts[s[i - len(p)]]
        
        # Check the last window
        if window_counts == target_counts:
            result.append(len(s) - len(p))

        return result

 
        # result = []
        # target, window = {}, {}
        # k = len(p)

        # for c in p:
        #     if c not in target:
        #         target[c] = 1
        #     else:
        #         target[c] += 1
        
        # for i in range(len(s)):
        #     if s[i] not in window:
        #         window[s[i]] = 1
        #     else:
        #         window[s[i]] += 1
            
        #     if i >= k:
        #         left_char = s[i - k]
        #         if window[left_char] == 1:
        #             del window[left_char]
        #         else:
        #             window[left_char] -= 1
            
        #     if window == target:
        #         result.append(i - k + 1)
        # return result
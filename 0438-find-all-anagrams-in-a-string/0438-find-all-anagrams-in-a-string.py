class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        k = len(p)
        n = len(s)
        target = collections.Counter(p)
        window = collections.Counter(s[:k - 1])

        for i in range(k - 1, n):
            if k > n:
                return result
            
            cur_char = s[i]
            window[cur_char] += 1

            if target == window:
                result.append(i - k + 1)
            
            window[s[i - k + 1]] -= 1
            if window [s[i - k + 1]] == 0:
                del window[s[i - k + 1]]
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
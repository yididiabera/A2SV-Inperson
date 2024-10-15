class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        longest_nice = ""

        for l in range(n):
            count = {}
            nice = True

            for r in range(l, n):
                char = s[r]
                count[char] = count.get(char, 0) + 1
                
                nice = True

                for c in count:
                    if c.islower() and c.upper() not in count:
                        nice = False
                    elif c.isupper() and c.lower() not in count:
                        nice = False
            
                if nice and r - l + 1 > len(longest_nice):
                    longest_nice = s[l: r + 1]

        return longest_nice

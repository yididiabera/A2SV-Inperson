class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        shift_effect = [0] * (n + 1)

        # Apply each shift to the shift_effect array
        for start, end, direction in shifts:
            delta = 1 if direction == 1 else -1
            shift_effect[start] += delta
            if end + 1 < n:
                shift_effect[end + 1] -= delta

        # Compute cumulative shifts
        cumulative_shift = 0
        for i in range(n):
            cumulative_shift += shift_effect[i]
            shift_effect[i] = cumulative_shift
        
        # Apply shifts to the string
        result = []
        for i, char in enumerate(s):
            # Compute new character with wrapping
            shift = shift_effect[i] % 26
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)

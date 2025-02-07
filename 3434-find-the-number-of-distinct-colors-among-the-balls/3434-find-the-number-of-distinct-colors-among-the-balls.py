class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color_map = {}  # Maps each ball to its color
        color_count = defaultdict(int)  # Tracks occurrences of each color
        color_set = set()  # Tracks distinct colors
        result = []

        for x, y in queries:
            if x in ball_color_map:
                old_color = ball_color_map[x]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    color_set.remove(old_color)

            # Assign the new color
            ball_color_map[x] = y
            color_count[y] += 1
            color_set.add(y)

            result.append(len(color_set))

        return result
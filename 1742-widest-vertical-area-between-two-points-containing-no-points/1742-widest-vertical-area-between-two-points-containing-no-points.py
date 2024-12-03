class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        _max = 0
        points.sort()
        x = [pt[0] for pt in points]
        for i in range(1, len(points)):
            _max = max(_max, x[i] - x[i - 1])
        return _max
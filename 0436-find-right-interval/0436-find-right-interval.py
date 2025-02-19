class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        # Store start value with its original index
        indexed_intervals = sorted((start, i) for i, (start, _) in enumerate(intervals))
        starts = [s[0] for s in indexed_intervals]  # Extract sorted start values
        res = []

        for _, end in intervals:
            idx = bisect_left(starts, end)  # Find the smallest start >= end
            if idx < len(starts):
                res.append(indexed_intervals[idx][1])  # Store the index of the right interval
            else:
                res.append(-1)  # No right interval found

        return res

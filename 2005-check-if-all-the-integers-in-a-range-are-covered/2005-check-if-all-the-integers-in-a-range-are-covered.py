class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        total = set()
        for ran in ranges:
            start, end = ran[0], ran[-1] + 1
            for i in range(start, end):
                total.add(i)
        print(total)
        # for i in range(len(ranges)):
        #     for j in range(len(ranges[i])):
        #         total.add(ranges[i][j])
        
        for i in range(left, right + 1):
            if i not in total:
                return False
        return True

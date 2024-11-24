class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #intialize variables and create a dict to count
        #add one fruit at a time and check if the selected fruit number is valid using a sliding window technique
        l = 0
        _max = 0
        count = collections.Counter()

        for r in range(len(fruits)):
            count[fruits[r]] += 1
            if len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            _max = max(_max, r - l + 1)
        return _max
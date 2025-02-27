class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        reminder = [0] * 60
        pairs = 0

        for t in time:
            rem = t % 60
            compliment = (60 - rem) % 60
            pairs += reminder[compliment]
            reminder[rem] += 1
            
        return pairs


        # count = 0
        # for i in range(len(time)):
        #     for j in range(i + 1, len(time)):
        #         if (time[i] + time[j]) % 60 == 0:
        #             count += 1
        
        # return count
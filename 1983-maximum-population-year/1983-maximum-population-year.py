class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        populations = [0] * 2051
        _max = 0
        result = 0
        for birth, death in logs:
            print(birth, death)
            populations[birth] += 1
            populations[death] -= 1

        curPop = 0
        for i, value in enumerate(populations):
            curPop += value
            if curPop > _max:
                _max = curPop
                result = i
        return result
        # for i in range(1, len(population)):
        #     population[i] = population[i - 1] + population[i]
        #     if population[i] > _max:
        #         _max = population[i]
        #         result = i
        # return i


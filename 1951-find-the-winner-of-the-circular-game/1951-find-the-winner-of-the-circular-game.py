class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = []
        k = k - 1
        for i in range(1,n + 1):
            players.append(i)
        size = len(players)
        i = 0
        while size > 1:
            i = (i + k) % size
            players.remove(players[i])
            size = len(players)
        
        return players[0]

        # i = 0
        # while len(n) > 1:
        #     i = (i + k) %
from collections import deque

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0
        q = deque([i for i in range(1, n+1)])
        while q:
            for _ in range(k-1):
                popped = q.popleft()
                if popped != 0:
                    q.append(popped)
            winner = q.popleft()
        return winner
        
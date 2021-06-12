class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # simple dp solution
        d = [0] + [float('inf')]*(amount)
        for coin in coins:
            for i in range(1,len(d)):
                if i-coin >= 0:
                    d[i] = min(d[i], d[i-coin] + 1)
        return d[amount] if d[amount] != float('inf') else -1
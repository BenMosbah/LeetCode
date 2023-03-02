class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        def dp(m, n):
            if n == 1:
                return 3 * 2 ** (m - 1)
            else:
                multiplier = 2 if m == 1 else 2 * m - 3 / 2
                return int(dp(m, n - 1) * (multiplier))

        return dp(m, n) % (10 ** 9 + 7)
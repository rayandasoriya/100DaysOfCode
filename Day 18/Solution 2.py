class Solution:
    def minPathSum(self, grid):
        """
            :type grid: List[List[int]]
            :rtype: int
            """
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                else:
                    upper_sum = dp[i-1][j] if i > 0 else float('inf')
                    left_sum = dp[i][j-1] if j > 0 else float('inf')
                    dp[i][j] = min(upper_sum, left_sum) + grid[i][j]
    return dp[-1][-1]

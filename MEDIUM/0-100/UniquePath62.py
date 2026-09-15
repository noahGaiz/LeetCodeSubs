class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(1)
            grid.append(row)

        for rows in range(1, len(grid)):
            for i in range(1, len(grid[0])):
                grid[rows][i] = grid[rows-1][i] + grid[rows][i-1]
        return grid[-1][-1]
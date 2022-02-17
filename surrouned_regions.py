class Solution:
    def solve(self, grid):
        x_len = len(grid)
        y_len = len(grid[0])
        for i in range(x_len):
            if grid[i][0] == 'O':
                self.dfs(grid, i, 0)

            if grid[i][y_len - 1] == 'O':
                self.dfs(grid, i, y_len - 1)

        for i in range(y_len):
            if grid[0][i] == 'O':
                self.dfs(grid, 0, i)

            if grid[x_len - 1][i] == 'O':
                self.dfs(grid, x_len - 1, i)

        for i in range(x_len):
            for j in range(y_len):
                if grid[i][j] == 'O':
                    grid[i][j] = 'X'

                if grid[i][j] == '*':
                    grid[i][j] = 'O'

        return grid

    def dfs(self, grid, x, y):
        x_len = len(grid)
        y_len = len(grid[0])
        queue = []
        queue.append((x, y))
        while queue:
            x1, y1 = queue.pop(0)
            grid[x1][y1] = '*'
            if x1 + 1 < x_len and grid[x1 + 1][y1] == 'O':
                queue.insert(0, (x1 + 1, y1))

            if y1 + 1 < y_len and grid[x1][y1 + 1] == 'O':
                queue.insert(0, (x1, y1 + 1))

            if x1 - 1 >= 0 and grid[x1 - 1][y1] == 'O':
                queue.insert(0, (x1 - 1, y1))

            if y1 - 1 >= 0 and grid[x1][y1 - 1] == 'O':
                queue.insert(0, (x1, y1 - 1))

board = [["O","O","O"],
         ["O","O","O"],
         ["O","O","O"]]

sol = Solution()
print(sol.solve(board))
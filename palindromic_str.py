class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        stack = []
        stack.append(Node(0, 0))
        total = 0
        while stack:
            node = stack.pop(0)
            if node.x == m - 1 and node.y == n - 1:
                total += 1

            if node.x + 1 < m:
                stack.insert(0, Node(node.x + 1, node.y))

            if node.y + 1 < n:
                stack.insert(0, Node(node.x, node.y + 1))
        return total


class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j - 1] + dp[j]
        return dp[-1] if m and n else 0


sol = Solution1()
total = sol.uniquePaths(10, 12)
print(total)



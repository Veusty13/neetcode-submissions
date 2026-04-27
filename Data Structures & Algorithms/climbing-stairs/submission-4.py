class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(nb_climbed_stairs, target):
            if nb_climbed_stairs == target:
                return 1
            if nb_climbed_stairs > target:
                return 0

            if nb_climbed_stairs in memo:
                return memo[nb_climbed_stairs]

            memo[nb_climbed_stairs] = (
                dfs(nb_climbed_stairs + 1, target)
                + dfs(nb_climbed_stairs + 2, target)
            )

            return memo[nb_climbed_stairs]

        return dfs(0, n)
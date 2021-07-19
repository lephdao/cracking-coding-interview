# Example of Knapsack problem
# Use Bottom-up and Tabulation

def solve_knapsack(profits, weights, capacity):
    # create a 2D array
    #
    n = len(profits)
    dp = [[0 for i in range(capacity+1)] for j in range(n)]
    max_profit = 0
    # fill the first row of dp table
    #
    for c in range(len(dp[0])):
        if c >= weights[0]:
            dp[0][c] = weights[0]

    # start tabulation
    #
    for i in range(1, n):
        for c in range(capacity+1):
            if c >= weights[i]:
                max_profit = max(dp[i - 1][c], profits[i] + dp[i - 1][c - weights[i]])
                dp[i][c] = max_profit
            else:
                dp[i][c] = dp[i - 1][c]

    print(dp)
    return max_profit

profits = [1,6,10,16]
weights = [1,2,3,5]
capacity = 7
print(solve_knapsack(profits, weights, capacity))

weights = [1,1,1,1,1]
profits = [1,2,3,4,5]
capacity = 3
print(solve_knapsack(profits, weights, capacity))
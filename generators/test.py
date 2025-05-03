def count_paths_with_obstacle(n, m, blocked_cell):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    bx, by = blocked_cell
    
    for i in range(n + 1):
        for j in range(m + 1):
            if (i, j) == blocked_cell:
                dp[i][j] = 0  # запрещённая клетка
            elif i == 0 and j == 0:
                dp[i][j] = 1  # стартовая точка
            else:
                from_top = dp[i - 1][j] if i > 0 else 0
                from_left = dp[i][j - 1] if j > 0 else 0
                dp[i][j] = from_top + from_left

    return dp[n][m]

print(count_paths_with_obstacle(3, 3, (1, 1)))  # 8
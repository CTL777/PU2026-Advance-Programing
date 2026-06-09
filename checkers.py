def solve():
    test_cases = [
        (4, ["....", "....", "....", "..W."]),
        (8, [".B.B.B..", "........", "........", "..B.....", "........", "..B.....", ".W......", "........"])
    ]
    MOD = 1000007

    for t_idx, (N, board) in enumerate(test_cases):
        board = board[::-1] # Row 0 is bottom
        start_pos = None
        for r in range(N):
            for c in range(N):
                if board[r][c] == 'W':
                    start_pos = (r, c)
                    break
            if start_pos: break

        dp = [[0] * N for _ in range(N)]
        dp[start_pos[0]][start_pos[1]] = 1

        for r in range(start_pos[0], N - 1):
            for c in range(N):
                if dp[r][c] == 0: continue
                
                # Try move left-up
                nr, nc = r + 1, c - 1
                if 0 <= nr < N and 0 <= nc < N:
                    if board[nr][nc] == '.':
                        dp[nr][nc] = (dp[nr][nc] + dp[r][c]) % MOD
                    elif board[nr][nc] == 'B':
                        nnr, nnc = r + 2, c - 2
                        if 0 <= nnr < N and 0 <= nnc < N and board[nnr][nnc] == '.':
                            dp[nnr][nnc] = (dp[nnr][nnc] + dp[r][c]) % MOD
                            
                # Try move right-up
                nr, nc = r + 1, c + 1
                if 0 <= nr < N and 0 <= nc < N:
                    if board[nr][nc] == '.':
                        dp[nr][nc] = (dp[nr][nc] + dp[r][c]) % MOD
                    elif board[nr][nc] == 'B':
                        nnr, nnc = r + 2, c + 2
                        if 0 <= nnr < N and 0 <= nnc < N and board[nnr][nnc] == '.':
                            dp[nnr][nnc] = (dp[nnr][nnc] + dp[r][c]) % MOD

        print(f"Case {t_idx + 1}: {sum(dp[N-1]) % MOD}")

solve()

NK = list(map(int, input().split(' ')))

dp = [0, 1, 1]
for i in range(3, NK[0] + 1):
    dp.append(0)
    if NK[1] < i:
        for j in range(NK[1], 0, -1):
            dp[i] = dp[i] + dp[i - j]
    else:
        for j in range(i - 1, 0, -1):
            dp[i] = dp[i] + dp[j]

print(dp[-1])
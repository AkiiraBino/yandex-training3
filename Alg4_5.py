N = int(input())

coor = list(map(int, input().split()))

coor.sort()

dp = [100001] * (N)
dp[1] = coor[1] - coor[0]

for i in range(2, N):
    dp[i] = min(dp[i - 2], dp[i - 1]) + coor[i] - coor[i-1]

print(dp[-1])
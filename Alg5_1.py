NM = list(map(int, input().split(' ')))

table = []

dp = [0] * NM[0]

for i in range(NM[0]):
    dp[i] = [0] * (NM[1])


for i in range(NM[0]):
    table.append(list(map(int, input().split(' '))))

dp[0][0] = table[0][0]

        
for i in range(NM[0]):
    for j in range(NM[1]):
        if i == 0 and j != 0:
            dp[i][j] = table[i][j] + dp[i][j - 1]
        elif i != 0 and j == 0:
            dp[i][j] = table[i][j] + dp[i - 1][j]
        elif i !=0 and j != 0:
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + table[i][j]

print(dp[-1][-1])
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
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + table[i][j]

path = []
i = NM[0] - 1
j = NM[1] - 1
while i != 0 or j != 0:
    if i == 0:
        path.append("R")
        j -= 1
    elif j == 0:
        path.append("D")
        i -= 1
    elif dp[i-1][j] > dp[i][j-1]:
        path.append("D")
        i -= 1
    else:
        path.append("R")
        j -= 1


print(dp[-1][-1])


print(' '.join(path[::-1]))

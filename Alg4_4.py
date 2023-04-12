ABC = [[4000, 4000, 4000]] * 3
dp = [0] * 3
[ABC.append(line.split(' ')) for line in open("input.txt")]
ABC.pop(3)
for i in range(3, len(ABC)):
    for j in range(len(ABC[i])):
        if ABC[i][j] != '\n':
            ABC[i][j] = int(ABC[i][j])
        else:
            ABC[i].pop(j)

for i in range(3, len(ABC)):
     dp.append(min(dp[i - 1] + ABC[i][0], dp[i-2] + ABC[i-1][1], dp[i-3] + ABC[i-2][2]))

print(dp[-1])

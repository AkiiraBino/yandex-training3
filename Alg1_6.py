M = int(input())

N = int(input())

part = []

for i in range(N):
    part[3] =(list(map(int, input().split(' '))))

    part[0] = min(part)
    part[1] = max(part)
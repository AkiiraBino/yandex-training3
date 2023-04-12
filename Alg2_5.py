num_city = int(input())

city = list(map(int, input().split(' ')))

stack = [city[0]]
index = [0]
result = [str(-1)] * num_city

for i in range(1, num_city):
    while city != [] and stack != [] and city[i] < stack[-1]:
        result[index.pop(-1)] = str(i)
        stack.pop(-1)
    stack.append(city[i])
    index.append(i)

print(' '.join(result))
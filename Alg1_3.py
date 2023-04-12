count_diego = int(input())
num_diego = set(map(int, input().split(' ')))
count_collect = int(input())
num_collect = list(map(int, input().split(' ')))

num_diego = sorted(list(num_diego))

def binary(elem, num_diego):
    middle = (len(num_diego) - 1) // 2
    left = 0
    result = -1
    right = len(num_diego) - 1
    while num_diego[middle] != elem and left <= right:
        if elem > num_diego[middle]:
            left = middle + 1
        else:
            right = middle - 1
        middle = (left + right) // 2
    if num_diego[middle] == elem:
        return middle, num_diego[middle]
    else:
        return [middle, -1]

for elem in num_collect:
    result = binary(elem, num_diego)
    if result[1] == -1:
        print(result[0] + 1)
    else:
        print(result[0])
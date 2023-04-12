NXT = list(map(int, input().split(' ')))

weight_s = list(map(int, input().split(' ')))

result = []

def nearest_value(items, value):
    found = items[0]
    index = 0
    for item in range(len(items)):
        if abs(items[item] - value) < abs(found - value):
            found = items[item]
            index = item
    return [found, index]

while NXT[2] != 0:
    value = nearest_value(weight_s, NXT[1])
    if NXT[2] - 
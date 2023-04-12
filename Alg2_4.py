count_cars = int(input())
cars_stack = list(map(int, input().split(' ')))

stack = []
final_stack = []

min = 1

while True:
    if cars_stack != [] and cars_stack[0] == min:
        final_stack.append(cars_stack.pop(0))
        min += 1

    elif stack != [] and stack[-1] == min:
        final_stack.append(stack.pop())
        min += 1

    elif cars_stack != []:
        stack.append(cars_stack.pop(0))

    elif cars_stack == [] and stack != [] and stack[-1] != min:
        break

    elif len(final_stack) == count_cars:
        break

if len(final_stack) == count_cars:
    print("YES")
else:
    print("NO")
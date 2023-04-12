str_pare = input()

stack = []
solution = True


for i in str_pare:
    if ord(i) in [40, 91, 123]:
        stack.append(ord(i))
    elif len(stack) != 0 and ord(i) in [stack[-1] + 1, stack[-1] + 2]:
        stack.pop()
    else:
        solution = False
        break

if len(stack) == 0 and solution:
    print("yes")
else:
    print("no")
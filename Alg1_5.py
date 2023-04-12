N = int(input())
array = [0] * (N)
for i in range(N):
    array[i] = int(input())

stack_keys = []
stack_values = []
count = 0

for i in range(len(array)):
    if stack_values == []:
        stack_values.append(array[i])
        stack_keys.append(i)

    elif stack_keys[-1] == (i - 1):

        if stack_values[-1] < array[i]:
            while stack_values[-1] < array[i]:
                count+=stack_values.pop(-1)
                stack_keys.pop(-1)
                stack_values.append(array[i])
                stack_keys.append(i)
        elif stack_values[-1] == array[i]:
            while stack_values != [] and stack_values[-1] == array[i]:
                count += stack_values.pop(-1)
                stack_keys.pop(-1)
            stack_values.append(array[i])
            stack_keys.append(i)
        else:
            count += array[i]
            stack_values.pop(-1)
            stack_keys.pop(-1)
            stack_keys.append(i)
            stack_values.append(array[i])

    else:
        stack_keys = [i]
        stack_values = [array[i]]



print(count)
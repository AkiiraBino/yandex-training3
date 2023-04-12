

stack = []
curr_value = 0.0
result = []
values = []

with open("input.txt") as file:
    values = file.readlines()
    values = [i.rstrip() for i in values]

va
#     while values != []:
#         if stack == []:
#             stack.append(values.pop(0))
#         elif  stack[-1] >= values[0]:
#             stack.append(values.pop(0))
#         elif stack != [] and stack[-1] < values[0] and stack[-1] > curr_value:
#             curr_value = stack.pop(-1)
#             while stack != [] and stack[-1] < values[0] and stack[-1] > curr_value:
#                 curr_value = stack.pop(-1)
#         else:
#             result.append(0)
#             break

#     while stack != []:
#         if stack[-1] > curr_value:
#             curr_value = stack.pop(-1)
#         elif len(result) < i + 1:
#             result.append(0)
#             break
#     if i + 1 > len(result):
#         result.append(1)

# for i in result:
#     print(i)

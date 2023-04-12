digit = []
exp = input()
exp = exp.split(' ')

for i in exp:
    if i.isdigit():
        digit.append(int(i))
    elif len(digit) >= 2:
        if i == "+":
            digit.append(digit.pop() + digit.pop())
        elif i == "-":
            digit.append(digit.pop(-2) - digit.pop(-1))
        elif i == "*":
            digit.append(digit.pop() * digit.pop())
    
print(digit[0])
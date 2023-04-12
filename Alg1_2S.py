REPLACE = int(input())
MYSTR = input()
maximum = 0
count = 1
replace_count = 0
lenght = len(MYSTR)
if lenght != 1:
    for i in range(lenght - 1):
        j = i + 1
        while j < lenght:
            if MYSTR[j] == MYSTR[i]:
                count += 1
                j += 1
            elif REPLACE - replace_count != 0:
                j += 1
                replace_count += 1
                
            else:
                maximum = max(maximum, (count + replace_count))
                count = 1
                replace_count = 0
                break

        if j > lenght:
            maximum = max(maximum, (count + replace_count))
            break
else:
    maximum = 1


print(maximum)
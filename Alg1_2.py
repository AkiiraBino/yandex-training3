REPLACE = int(input())
MYSTR = input()
lenght = len(MYSTR)
maximum = 0

for symbol in range(97, 123):
        j = 0
        symbol = chr(symbol)
        
        for i in range(lenght):
            while REPLACE >= 0 and j != lenght:
                if MYSTR[j] != symbol and REPLACE != 0:
                    REPLACE -= 1
                    j += 1
                elif MYSTR[j] != symbol and REPLACE == 0:
                    break
                else:
                    j += 1
            maximum = max(len(MYSTR[i:j]), maximum)
            if MYSTR[i] != symbol:
                REPLACE += 1

print(maximum)
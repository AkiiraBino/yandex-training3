mystr = str()

with open("input.txt") as file:
    mystr = file.read()


def count(mystr):
    countChar = dict()
    
    for i in range(len(mystr)):
        
        if mystr[i] in countChar.keys():
            countChar[mystr[i]] += 1

        else:
            countChar[mystr[i]] = 1

    return countChar


def clear(countChar):
    try:
        countChar.pop(' ')
        countChar.pop('\n')
        return countChar
    except KeyError:
        try:
            countChar.pop('\n')
            return countChar
        except KeyError:
            return countChar


def sortKeys(countChar):
    mystr = dict()

    while countChar != dict():
        minimal = min(countChar.keys())
        mystr[minimal] = countChar[minimal]
        countChar.pop(minimal)

    return mystr


             
def createGrids(countChar):
    histLine = []
    count = list(countChar.values())
    hist = []
    maximum = max(count)

    for line in range(maximum):
        for column in countChar.values():
            if column >= maximum:
                histLine.append('#')

            else:
                histLine.append(' ')
        if line == 0:
            hist.append(''.join(histLine))
        else:
            hist.append('\n')
            hist.append(''.join(histLine))
        histLine = list()
        maximum -= 1
    hist.append('\n')
    hist.append(''.join(list(countChar.keys())))

    return ''.join(hist)


mystr = count(mystr)

mystr = clear(mystr)

mystr = sortKeys(mystr)

with open("output.txt", 'w') as file:
    file.write(createGrids(mystr))
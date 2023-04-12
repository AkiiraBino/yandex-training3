
def heapify(array, lenght, i = 0):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < lenght and array[largest] < array[left]:
        largest = left
    try:
        if right < lenght and array[largest] < array[right]:
            largest = right
    except IndexError:
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            heapify(array, lenght, largest)
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, lenght, largest)



def exctract(array, lenght):
    maximum = array[0]
    array[0] = array[-1]
    heapify(array, lenght)
    array.pop(-1)
    return maximum


lenght = int(input())
array = list(map(int, input().split(' ')))


for i in range(lenght//2, -1, -1):
    heapify(array, lenght, i)


result = []


for i in range(lenght):
    result.append(str(exctract(array, lenght - i)))


print(' '.join(result[::-1]))
text = [line.split(' ') for line in open('input.txt')]
first = list(map(int, [line for line in text[0]][:5]))
second = list(map(int, [line for line in text[1]][:5]))


count = 0
FINISH = 10**6



class Queue:
    def __init__(self):
        self.array = []

    def push(self, n):
        self.array.append(n)

    def pop(self):
        if self.array != []:
            return(self.array.pop(0))

    def front(self):
        if self.array != []:
            return(self.array[0])

    def size(self):
        return(len(self.array))

    def clear(self):
        self.array = []

queue_first = Queue()
queue_second = Queue()

for i in range(5):
    queue_first.push(first[i])
    queue_second.push(second[i])

while queue_first.size() != 0 and queue_second.size() != 0 and count != FINISH:
    if queue_first.front() not in [0, 9] or queue_second.front() not in [0, 9]:
        if queue_first.front() > queue_second.front():
            queue_first.push(queue_first.pop())
            queue_first.push(queue_second.pop())
        elif queue_second.front() > queue_first.front():
            queue_second.push(queue_first.pop())
            queue_second.push(queue_second.pop())
    else:
        if queue_first.front() == 0:
            queue_first.push(queue_first.pop())
            queue_first.push(queue_second.pop())
        else:
            queue_second.push(queue_first.pop())
            queue_second.push(queue_second.pop())    
    count+=1

if queue_first.size() == 0 and count != 10**6:
    print("second", count)
elif queue_second.size() == 0 and count != 10**6:
    print("first", count)
else:
    print("botva")
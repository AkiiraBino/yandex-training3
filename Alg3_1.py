class Queue:
    def __init__(self):
        self.array = []

    def push(self, n):
        self.array.append(n)
        print("ok")

    def pop(self):
        if self.array != []:
            print(self.array.pop(0))
        else:
            print("error")
    
    def front(self):
        if self.array != []:
            print(self.array[0])
        else:
            print("error")

    def size(self):
        print(len(self.array))

    def clear(self):
        self.array = []
        print("ok")

queue = Queue()

while True:
    command = input()

    if "push" in command.split(' '):
        queue.push(command.split(' ')[1])
    elif "pop" == command:
        queue.pop()
    elif "front" == command:
        queue.front()
    elif "size" == command:
        queue.size()
    elif "clear" == command:
        queue.clear()
    elif "exit" == command:
        print("bye")
        break
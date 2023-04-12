class Deque:
    def __init__(self):
        self.array = []

    def push_front(self, n):
        self.array.insert(0, n)
        print("ok")

    def push_back(self, n):
        self.array.append(n)
        print("ok")

    def pop_front(self):
        if self.array != []:
            print(self.array.pop(0))
        else:
            print("error")

    def pop_back(self):
        if self.array != []:
            print(self.array.pop())
        else:
            print("error")
    
    def front(self):
        if self.array != []:
            print(self.array[0])
        else:
            print("error")

    def back(self):
        if self.array != []:
            print(self.array[-1])
        else:
            print("error")

    def size(self):
        print(len(self.array))

    def clear(self):
        self.array = []
        print("ok")


deque = Deque()


while True:
    
    command = input()

    if "push_back" in command.split(' '):
        deque.push_back(command.split(' ')[-1])
    elif "push_front" in command.split(' '):
        deque.push_front(command.split(' ')[-1])
    elif "pop_front" == command:
        deque.pop_front()
    elif "pop_back" == command:
        deque.pop_back()
    elif "front" == command:
        deque.front()
    elif "back" == command:
        deque.back()
    elif "size" == command:
        deque.size()
    elif "clear" == command:
        deque.clear()
    elif "exit" == command:
        print("bye")
        break
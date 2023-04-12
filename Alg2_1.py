class Stack:

    def __init__(self) -> None:
        self.stack = []
    
    def push(self, n):
        self.stack.append(n)
        print("ok")
    
    def back(self):
        if self.stack != []:
            print(self.stack[-1])
        
        else:
            print("error")

    def pop(self):
        if self.stack != []:
            print(self.stack[-1])
            self.stack.pop()

        else:
            print("error")
    
    def size(self):
        print(len(self.stack))

    def clear(self):
        self.stack = []
        print("ok")

leave = True
stack = Stack()
while leave:
    command = input()
    if "push" in command:
        stack.push(command.split(' ')[-1])
    elif "back" == command:
        stack.back()
    elif "size" == command:
        stack.size()
    elif "clear" == command:
        stack.clear()
    elif "pop" == command:
        stack.pop()
    elif "exit" == command:
        leave = False
        print("bye")
class Heap:
    def __init__(self):
        self.array = []

    def insert(self, n):
        self.array.append(n)
        self.sifting_up()

    def sifting_up(self):
        index = len(self.array) - 1
        index_father = (index-1)//2
        while index != 0 and self.array[index] > self.array[index_father]:
            self.array[index], self.array[index_father] =\
                self.array[index_father], self.array[index]
            index, index_father = index_father, (index_father-1)//2

    def exctract(self):
        print(self.array[0])
        self.array[0] = self.array[-1]
        self.sifting_down()
        self.array.pop()

    def sifting_down(self):
        index = 0
        index_children = [(index * 2) + 1, (index * 2) + 2]
        while index_children[0] < (len(self.array) - 1) and\
                (self.array[index_children[0]] > self.array[index] or
                self.array[index_children[1]] > self.array[index]):
            if self.array[index_children[0]] > self.array[index_children[1]]:
                self.array[index], self.array[index_children[0]] =\
                    self.array[index_children[0]], self.array[index]
                index, index_children[0], index_children[1] =\
                    index_children[0], (index_children[0] * 2) + 1, (index_children[0] * 2) + 2
            else:
                self.array[index], self.array[index_children[1]] =\
                    self.array[index_children[1]], self.array[index]
                index, index_children[0], index_children[1] =\
                    index_children[1], (index_children[1] * 2) + 1, (index_children[1] * 2) + 2

count = int(input())
heap = Heap()


for i in range(count):
    command = list(map(int, input().split()))
    if command[0] == 0:
        heap.insert(command[1])
    else:
        heap.exctract()
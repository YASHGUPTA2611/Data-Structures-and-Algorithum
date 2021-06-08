from collections import deque

class queue():

    def __init__(self):
        self.buffer = deque()

    def add(self,value):
        return self.buffer.appendleft(value)

    def exit(self):
        return self.buffer.pop()

    def zero(self):
        return len(self.buffer)==0
    def len(self):
        return len(self.buffer)

q = queue()
q.add([5,10,15])
q.add([20,25,30])
q.add([35,40,45])
print(q.len())
print(q.exit())
print(q.exit())

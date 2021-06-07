from collections import deque

class Stack:


    def __init__(self):

        self.container = deque()

    def push(self,val):
        return self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def len(self):
        return len(self.container) 

def reverse_string(s):

    stack = Stack()

    for i in s:
        stack.push(i)
    string = ''
    while stack.len()!=0:
        string += stack.pop()
    return string

if __name__ == '__main__':
    print(reverse_string("We will conquere COVI-19"))
    print(reverse_string("I am the king"))






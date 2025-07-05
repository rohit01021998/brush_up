'''
Same as singly linked list but names will change.
Stack is last in first out like a tennis ball container.
Functionalities: print_stack, push and pop.
Node will have value and next.
Stack will have top and bottom, out of which only top will be used.
Instead of length we will have height.

TOP (Not used)
|
v
Node
|
v
Node
|
v
Node
|
v
Node
|
v
BOTTOM (Not used)
|
v
None

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def push_to_stack(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
            self.height += 1
        elif self.height > 0:
            new_node.next = self.top
            self.top = new_node
            self.height += 1
        else:
            print('Some error occured!')

    def pop_from_stack(self):
        if self.height==0:
            self.top = None
            self.height -= 1
        elif self.height > 0:
            self.top = self.top.next
            self.height -= 1
        else:
            print('Some error occured!')

    def print_stack(self):
        print('Top of the stack')
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print('Bottom of the stack')

def main():
    new_stack = Stack(999)
    for i in range(5):
        new_stack.push_to_stack(i)
    new_stack.push_to_stack(998)
    new_stack.print_stack()
    new_stack.pop_from_stack()
    new_stack.print_stack()

if __name__ == '__main__':
    main()
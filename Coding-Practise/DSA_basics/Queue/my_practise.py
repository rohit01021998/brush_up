'''
Same as singly linked list but names will change.
Queue is first in first out like a queue line for a counter.
Functionalities: Print_queue, Queue and Dequeue.
Node will have value and next.
Queue will have first and last.

first node (Dequeue happens here) -> node -> node -> node -> last node (Enqueue happens here)-> None
'''

class Node:
    def __init__(self,value):
        # print('Node is created!')
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        # print('Queue is created!')
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def enqueue(self, value):
        # print('Enqueue is running!')
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
            self.length += 1
        elif self.length > 0:
            self.last.next = new_node
            self.last = new_node
            self.length += 1
        else:
            print('Some Error Occured!')
        return True
        
    def dequeue(self):
        # print('deque is running!')
        if self.length == 0:
            print('No element is available to remove!')
        elif self.length > 0:
            temp = self.first
            self.first = self.first.next
            temp.next = None
            self.length -= 1
        else:
            print('Some Error Occurred!')
        return True
    
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

def main():
    # print('Main is running!')
    new_queue = Queue(999)
    for i in range(5):
        new_queue.enqueue(i)
    new_queue.enqueue(998)
    new_queue.print_queue()
    new_queue.dequeue()
    new_queue.dequeue()
    new_queue.dequeue()
    new_queue.dequeue()
    print('\n')
    new_queue.print_queue()

if __name__ == '__main__':
    main()
'''
1. Features to add: append, pop, prepend, pop_first, get, set_value, print_list, insert (at index), remove (at index), reverse.
2. Thought Process: Think of features need in Node (value, next) > Think of features present in LinkedList (Node, head, tail, temp/node_before_temp)
3. Reversing a linkedlist requires three variables: before-temp-after.

head  next              Tail
   *   ->   *  ->  *  ->  *
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        self.node_to_append = Node(value)
        if self.length==0:
            self.head = self.node_to_append
            self.tail = self.node_to_append
            self.length+=1
            return [self.tail, self.tail.value]
        else:
            self.tail.next = self.node_to_append
            self.tail = self.node_to_append
            self.length+=1
            return [self.tail, self.tail.value]

    def pop(self):
        if self.length==0:
            print('No element to remove!')
            return False
        elif self.length==1:
            self.temp = self.head
            self.head=None
            self.tail=None
            self.length -= 1
            return [self.temp, self.temp.value]

        else:
            self.temp = self.head
            self.one_node_before_temp = self.head
            while self.temp.next is not None:
                self.one_node_before_temp = self.temp
                self.temp = self.temp.next
            self.tail = self.one_node_before_temp
            self.tail.next = None
            self.length -= 1
            return [self.temp, self.temp.value]
    
    def prepend(self, value):
        self.prepend_node = Node(value)
        if self.length == 0:
            self.head = self.prepend_node
            self.tail = self.prepend_node
            self.length += 1
            return [self.head, self.head.next]
        elif self.length != 0:
            self.prepend_node.next = self.head
            self.head = self.prepend_node
            self.length += 1
            return [self.head, self.head.next]
    
    def pop_first(self):
        if self.length == 0:
            print('No element is present in the Linked List')
            return False
        elif self.length == 1:
            self.temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return [self.temp, self.temp.value]
        else:
            self.temp = self.head
            self.head = self.head.next
            self.temp.next = None
            self.length -= 1
            return [self.temp, self.temp.value]
        
    def get(self, index):
        self.temp = self.head
        if (index + 1) > self.length or (index) < 0:
            print("ERROR: Index Not Present!")
            return False
        else:
            for _ in range(index):
                self.temp = self.temp.next
            print(self.temp.value)
            return self.temp, self.temp.value
        
    def set_value(self, index, value):
        node, _ = self.get(index)
        node.value = value
        return node, node.value
    
    def insert(self, index, value):
        self.new_node = Node(value)
        self.temp = self.head
        self.node_before_temp = self.head
        if (index+1) > self.length or index < 0:
            print('Invalid index')
            return False
        else:
            for _ in range(index):
                self.node_before_temp = self.temp
                self.temp = self.temp.next
            self.node_before_temp.next = self.new_node
            self.new_node.next = self.temp
            self.length += 1
            print(self.length)
            return [self.new_node, self.new_node.value]
    
    def remove(self, index):
        self.temp = self.head
        self.node_before_temp = self.head
        if (index+1) > self.length or index < 0:
            print('Invalid index')
            return False
        else:
            for _ in range(index):
                self.node_before_temp = self.temp
                self.temp = self.temp.next
            self.node_before_temp.next = self.temp.next
            self.temp.next = None
            self.length -= 1
            return [self.temp, self.temp.value]
    
    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head  # The old head becomes the new tail
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        return True

    def print_list(self):
        self.temp = self.head
        print('# LL Start #')
        if self.length != 0:
            while self.temp is not None:
                print(self.temp.value, id(self.temp.value))
                self.temp = self.temp.next
        else:
            print('List is empty!')
        print('# LL End #')

def main():
    NewLL = LinkedList(1)
    NewLL.pop()
    NewLL.pop()
    NewLL.prepend(999)
    NewLL.prepend(10101)
    NewLL.pop_first()
    for i in range(10):
        NewLL.append(i)
        
    NewLL.print_list()
    NewLL.get(5) # 4
    NewLL.set_value(5,69)
    NewLL.print_list()

    NewLL.insert(5,68)
    NewLL.print_list()
    NewLL.remove(6)
    NewLL.reverse()
    NewLL.print_list()

if __name__ == '__main__':
    main()
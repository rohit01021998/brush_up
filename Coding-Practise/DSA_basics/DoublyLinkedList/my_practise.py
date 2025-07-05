'''
1. Features to add: print_list, append, prepend, pop, pop_first, get, set_value, insert (at index), remove (at index).
2. Thought Process: Think of features need in Node (value, next, prev) > Think of features present in LinkedList (Node, head, tail, temp/node_before_temp)
3. Reversing a linkedlist requires three variables: before-temp-after.

       head  next/prev              Tail
     <- *       <=>   *  <=>  *  <=>  * -> None
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class doubly_linked_list():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length=1
    
    def print_list(self):
        if self.length == 0:
            print('No element present in the linked list!')
        elif self.length != 0:
            temp = self.head
            for _ in range(self.length):
                print(temp.value)
                temp = temp.next
        return True
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        elif self.length >= 1:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1
        else:
            print('Some problem occured!')
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        elif self.length >= 1:
            self.head.prev = self.head
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        else:
            print('Some problem occured!')
        return True
    
    def pop(self):
        if self.length == 0:
            print('No element present in the linked list to pop')
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.length >= 1:
            temp = self.tail.prev
            temp.next = None
            self.tail.prev = None
            self.tail = temp
            self.length -= 1
        else:
            print('Some Problem occured')
        return True

    def pop_first(self):
        if self.length == 0:
            print('No element present in the linked list to pop')
        elif self.length >= 1:
            temp = self.head.next
            temp.prev = None
            self.head.next = None
            self.head = temp
            self.length -= 1
        else:
            print('Some problem occured')
        return True
    
    def get_value(self, index):
        if index < 0 or index > (self.length-1):
            print('Invalid Index')
        else:
            if index <= (self.length+1)/2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
                print(temp.value)
                return temp
            else:
                temp = self.tail
                for _ in range(self.length-1, 0 , -1):
                    temp = temp.prev
                print(temp.value)
                return temp
        return True
    
    def set_value(self, index, value):
        temp = self.get_value(index)
        if temp is not None:
            temp.value = value
        return True
    
    def insert_value(self, index, value):
        new_node = Node(value)
        temp = self.get_value(index)
        if temp is not None:
            node_before_temp = temp.prev
            node_before_temp.next = new_node
            new_node.prev = node_before_temp
            temp.prev = new_node
            new_node.next = temp
            self.length += 1
        else:
            print('Some Error Occured')
        return True
    
    def remove_value(self, index):
        temp = self.get_value(index)
        if temp is not None:
            node_before_temp = temp.prev
            node_after_temp = temp.next
            node_before_temp.next = node_after_temp
            node_after_temp.prev = node_before_temp
            temp.prev = None
            temp.next = None
            self.length -= 1
            return True


def main():
    NewLL = doubly_linked_list(1)
    # NewLL.print_list()
    # NewLL.pop()
    # NewLL.print_list()
    # NewLL.pop()
    # NewLL.prepend(999)
    # NewLL.prepend(10101)
    # NewLL.print_list()
    # NewLL.pop_first()
    for i in range(5):
        NewLL.append(i)
    # NewLL.print_list()
    # NewLL.get_value(3) # 4
    NewLL.print_list()
    NewLL.set_value(3,69)
    NewLL.print_list()

    NewLL.insert_value(3,68)
    # NewLL.print_list()
    NewLL.remove_value(3)
    NewLL.print_list()

if __name__=='__main__':
    main()
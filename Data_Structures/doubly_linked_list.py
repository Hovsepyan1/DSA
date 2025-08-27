class Node:
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next 
        self.size = 0
        
class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def push_back(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = self.tail.next 
        self.size += 1
    
    def push_front(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return 
        new_node.next = self.head
        self.head.prev = new_node
        self.head = self.head.prev
        self.size += 1
    
    def pop_back(self):
        if not self.head:
            return 
        elif not self.head.next:
            self.head = None
            self.tail = None
            self.size -= 1
            return
        
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
    
    def pop_front(self):
        if not self.head:
            return 
        elif not self.head.next:
            self.head = self.head.next
            size -= 1
            return
        
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1 
        

    def search(self, val):
        tmp = self.head
        while tmp:
            if tmp.val == val:
                return True
            
        return False
    
    def insert(self, pos, val):
        if pos > self.size:
            print("Invalid Position")
            return 
        elif pos == 0:
            self.push_front(val)
            return
        elif pos == self.size:
            self.push_back(val)
            return
            
        new_node = Node(val)
        i = 0
        tmp = self.head
        while i < pos - 1:
            tmp = tmp.next
            i += 1
        
        new_node.next = tmp.next
        tmp.next = new_node
        new_node.prev = tmp
        new_node.next.prev = new_node
        self.size += 1
        print("End of insert function")
        
    def erase(self, pos):
        if pos > self.size:
            print("Invalid Position")
            return 
        elif pos == 0:
            self.pop_front()
            return
        elif pos == self.size:
            self.pop_back()
            return
        
        i = 0
        tmp = self.head
        while i < pos:
            tmp = tmp.next 
            i += 1
            
        tmp.prev.next = tmp.next
        tmp.next.prev = tmp.prev
            
    
    def print_forward(self):
        if not self.size:
            print("Linked list is empty")
            return
        tmp = self.head
        while tmp:
            print(tmp.val, end="->")
            tmp = tmp.next
        print()
            
    def print_backward(self):
        if self.size == 0:
            print("Linked list is empty")
            return
        tmp = self.tail
        while tmp:
            print(tmp.val, end="->")
            tmp = tmp.prev
        print()
            
dll = Doubly_Linked_List()
dll.print_forward()
dll.print_backward()
# dll.push_back(1)
# dll.push_front(2)
# dll.print_forward()
# dll.print_backward()
# dll.pop_back()
# dll.print_forward()
# dll.print_backward()
# dll.pop_back()
# dll.print_forward()
# dll.print_backward()
# dll.pop_back()
# dll.print_forward()
# dll.print_backward()
# dll.push_back(2)
# dll.push_back(3)
# dll.push_back(4)
# dll.print_forward()
# print("---------")
# dll.print_backward()


# dll.push_front(5)
# dll.print_forward()
# dll.print_backward()
# dll.pop_back()
# dll.print_forward()
# dll.print_backward()

dll.push_back(1)
dll.push_back(2)
dll.push_front(3)
dll.push_front(4)
print(dll.head.val)
print(dll.tail.val)
dll.print_forward()
dll.print_backward()
dll.insert(4, 10)
dll.print_forward()
dll.print_backward()
print(dll.size)
dll.erase(5)
dll.print_forward()
dll.print_backward()
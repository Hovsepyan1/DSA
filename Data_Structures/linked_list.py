class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None  
    
    def is_empty(self):
        return self.head == None
    
    def push_back(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        tmp = self.head
        while tmp.next != None:
            tmp = tmp.next
            
        tmp.next = new_node
    
    def push_front(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    
    def insert_after(self, prev_node, data):
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def remove(self, key):
        if self.head is None: 
            return

        if self.head.data == key:  
            self.head = self.head.next
            return True

        tmp = self.head
        while tmp.next and tmp.next.data != key:
            tmp = tmp.next

        if tmp.next:  
            tmp.next = tmp.next.next
            return tmp.data
        return None
    
    def search(self, key):
        tmp = self.head
        while tmp != None:
            if tmp.data == key:
                return True
            tmp = tmp.next
            
        return False
    
    def length(self):
        tmp = self.head
        count = 0
        while tmp != None:
            tmp = tmp.next
            count += 1
            
        return count
    
    def display(self):
        tmp = self.head
        while tmp != None:
            print(tmp.data, end = "->")
            tmp = tmp.next
        
    def __str__(self):
        return f"{self.display()}"
        

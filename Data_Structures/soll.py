class Node:
    def __init__(self, val = 0, prev = None, next = None, desc = None, asc = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.desc = desc
        self.asc = asc
        
class SOLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.descHead = None
        self.ascHead = None
        self.size = 0
        
    def putInSortedOrder(self, node):
        if not node:
            return
        if not self.ascHead or not self.descHead:  
            self.ascHead = node
            self.descHead = node
            return
        
        if node.val <= self.ascHead.val:
            node.desc = self.ascHead
            self.ascHead.asc = node
            self.ascHead = node
            return
        
        if node.val >= self.descHead.val:
            node.asc = self.descHead
            self.descHead.desc = node
            self.descHead = node
            return
        
        current = self.ascHead
        while current.desc and current.desc.val < node.val:
            current = current.desc
        
        node.desc = current.desc
        if current.desc:
            current.desc.asc = node
        current.desc = node
        node.asc = current

        
    def remove_sorted_order(self, node):
        if not node:
            return

        if self.ascHead == node and self.descHead == node:
            self.ascHead = None
            self.descHead = None
            return

        if self.ascHead == node:
            self.ascHead = node.desc
            if self.ascHead:
                self.ascHead.asc = None
        elif self.descHead == node:
            self.descHead = node.asc
            if self.descHead:
                self.descHead.desc = None
        else:
            if node.asc:
                node.asc.desc = node.desc
            if node.desc:
                node.desc.asc = node.asc

        
    
    def push_back(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            self.putInSortedOrder(new_node)
            return
        
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.size += 1
        self.putInSortedOrder(new_node)
        
    def push_front(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            self.putInSortedOrder(new_node)
            return 
        new_node.next = self.head
        self.head.prev = new_node
        self.head = self.head.prev
        self.size += 1
        self.putInSortedOrder(new_node)
        
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
        # print("End of insert function")
        self.putInSortedOrder(new_node)
        
    def pop_back(self):
        if not self.head:
            return 
        elif not self.head.next:
            self.head = None
            self.tail = None
            self.size -= 1
            return
        
        self.remove_sorted_order(self.tail)
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
        
        self.remove_sorted_order(self.head)
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1 
        
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
        
        self.remove_sorted_order(tmp)
        tmp.prev.next = tmp.next
        tmp.next.prev = tmp.prev
        self.size -= 1
        
    def search(self, val):
        tmp = self.head
        while tmp:
            if tmp.val == val:
                return True
            tmp = tmp.next
            
        return False
        
    def print_forward(self):
        if self.size == 0:
            print("List is empty")
            return
        tmp = self.head
        while tmp:
            print(tmp.val, end="<->")
            tmp = tmp.next
        print()
            
    def print_backward(self):
        if self.size == 0:
            print("List is empty")
            return
        tmp = self.tail
        while tmp:
            print(tmp.val, end="<->")
            tmp = tmp.prev
        print()
            
    def print_descending_order(self):
        if self.size == 0:
            print("List is empty")
            return
        tmp = self.descHead
        while tmp:
            print(tmp.val, end="<->")
            tmp = tmp.asc
        print()
        
    def print_ascending_order(self):
        if self.size == 0:
            print("List is empty")
            return
        tmp = self.ascHead
        while tmp:
            print(tmp.val, end="<->")
            tmp = tmp.desc
        print()
            
soll = SOLL() 
soll.push_back(1)
print("descHead = ",soll.descHead.val)
print("ascHead = ",soll.ascHead.val)
soll.push_back(2)
soll.print_ascending_order()
soll.print_descending_order()
# print("descHead = ",soll.descHead.val)
# print("ascHead = ",soll.ascHead.val)
soll.push_back(3)
soll.print_ascending_order()
soll.print_descending_order()
soll.push_front(0)
soll.print_ascending_order()
soll.print_descending_order()
# soll.print_forward()
# soll.print_backward()
# print("---")
# print(soll.descHead.val)
# print(soll.ascHead.val)
# print("descHead = ",soll.descHead.val)
# print("ascHead = ",soll.ascHead.val)
# soll.print_ascending_order()
# soll.print_descending_order()
soll.insert(2, 10)
soll.print_forward()
soll.print_backward()
soll.print_ascending_order()
soll.print_descending_order()
soll.pop_back()
print("pop back")
soll.print_forward()
soll.print_backward()
soll.print_ascending_order()
soll.print_descending_order()
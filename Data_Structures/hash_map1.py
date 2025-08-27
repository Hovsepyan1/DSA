class Node:
    def __init__(self, key = 0, value = 0, next = None):
        self.key = key
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def push_front(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
                
    def remove(self, key):
        prev = None
        curr = self.head
        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return curr.value  
            prev = curr
            curr = curr.next
        return None 
        
    def search(self, key):
        tmp = self.head
        while tmp:
            if tmp.key == key:
                return True
            tmp = tmp.next
        return False
        
    def is_empty(self):
        return self.head == None
    
    
class HashMap:
    def __init__(self):
        self.table_size = 7
        self.items_count = 0
        self.load_factor = 0.75
        self.table = [LinkedList() for i in range(self.table_size)]
        
    def __hash(self, key):
        return  hash(key)
    
    def __rehash(self):
        old_table = self.table
        self.table_size = self.__getNextPrimeNumber(self.table_size)
        self.table = [LinkedList() for i in range(self.table_size)]
        self.items_count = 0
        
        for bucket in old_table:
            if not bucket.is_empty():
                node = bucket.head
                while node:
                    self.insert(node.key, node.value)
                    node = node.next
    
    def insert(self, key, value):
        index = self.__hash(key) % self.table_size
        if self.table[index].search(key):
            node = self.table[index].head
            while node:
                if node.key == key:
                    node.value = value
                    return
        
        self.table[index].push_front(key, value)
        self.items_count += 1
        
        if (self.items_count / self.table_size) > self.load_factor:
            self.__rehash()
            
    def search(self, key):
        index = self.__hash(key) % self.table_size
        if not self.table[index].is_empty():
            node = self.table[index].head
            while node:
                if node.key == key:
                    return node.value
                node = node.next
                
        return None
    
    def remove(self, key):
        index = self.__hash(key) % self.table_size
        if self.table[index].search(key):
            self.table[index].remove(key)
        else:
            raise KeyError("Invalid Key!")
            
    def __getNextPrimeNumber(self, num):
        def isPrime(num):
            if num < 2:
                return False
            
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            
            return True
        
        next_num = 0
        while True:
            num = num + 1
            if isPrime(num):
                return num
            
    def __getitem__(self, key):
        index = self.__hash(key) % self.table_size
        if not self.table[index].is_empty():
            tmp = self.table[index].head
            while tmp:
                if tmp.key == key:
                    return tmp.value
                tmp = tmp.next
        raise KeyError("Invalid Key!")
    
    def __setitem__(self, key, value):
        self.insert(key, value)
        
    def __iter__(self):
        for bucket in self.table:
            if not bucket.is_empty():
                node = bucket.head
                while node:
                    yield node.key, node.value
                    node = node.next
            
            

def test_hash_map():
    hm = HashMap()

    hm['a'] = 9
    assert hm['a'] == 9, "Test case 1 failed: Insert or retrieve failed."

    hm['a'] = 10
    assert hm['a'] == 10, "Test case 2 failed: Update failed."

    hm['b'] = 15
    hm['c'] = 20
    hm['d'] = 25
    assert hm['b'] == 15, "Test case 3 failed: Key 'b' not found."
    assert hm['c'] == 20, "Test case 3 failed: Key 'c' not found."
    assert hm['d'] == 25, "Test case 3 failed: Key 'd' not found."

    assert hm.search('b') == 15, "Test case 4 failed: Search failed for key 'b'."
    assert hm.search('z') is None, "Test case 4 failed: Search returned value for non-existent key 'z'."

    hm.remove('c')
    assert hm.search('c') is None, "Test case 5 failed: Key 'c' was not removed."
    try:
        hm['c']
    except KeyError:
        pass
    else:
        raise AssertionError("Test case 5 failed: KeyError not raised for accessing removed key.")

    for i in range(10):
        hm[f'key_{i}'] = i
    assert hm.table_size > 7, "Test case 6 failed: Rehashing did not occur."

    keys = set()
    values = set()
    for key, value in hm:
        keys.add(key)
        values.add(value)
    assert 'a' in keys and 10 in values, "Test case 7 failed: Iteration failed."

    try:
        hm.remove('z')
    except KeyError:
        pass  
    else:
        raise AssertionError("Test case 8 failed: KeyError not raised for non-existent key removal.")

    print("All test cases passed!")

test_hash_map()

from linked_list import LinkedList

class HashSet:
    def __init__(self):
        self.table_size = 7
        self.table = self.init_table()
        self.load_factor = 0.75
        self.items_count = 0
        
    def init_table(self):
        ls = []
        for i in range(self.table_size):
            ls.append(LinkedList())
        return ls
        
    def __hash(self, key):
        key = key * 31 
        key = (key ^ (key >> 16)) & 0xffffffff 
        key = (key * 21) & 0xffffffff 
        key = (key ^ (key >> 11)) & 0xffffffff 
        key = (key + (key << 4)) & 0xffffffff 

        return key % len(self.table) 
    
    def __rehash(self):
        self.table_size = self.getNextPrimeNumber(self.table_size * 2)
        old_table = self.table
        self.table = self.init_table()
        self.items_count = 0
        for item in old_table:
            if not item.is_empty():
                tmp = item.head
                while tmp:
                    self.insert(tmp.data)
                    tmp = tmp.next

        
    def getNextPrimeNumber(self, num):
        def isPrime(num):
            if num <= 2:
                return False
            
            i = 2
            while i <= num // 2:
                if num % i == 0:
                    return False
                i += 1
                
            return True
        next_num = 0
        while True:
            num += 1
            if isPrime(num):
                next_num = num
                break
        
        return next_num
    
    def search(self, value):
        index = self.__hash(value)
        return self.table[index].search(value)
    
    def insert(self, val):
        index = self.__hash(val)
        # print(index)
        self.table[index].push_front(val)
        self.items_count += 1
        
        if (self.items_count / len(self.table)) >= self.load_factor:
            self.__rehash()
    
    def remove(self, value):
        index = self.__hash(value)
        if self.table[index].remove(value):
            print("Element removed succesfully")
        else:
            raise ValueError("There is no such element")

hs = HashSet()
# print(hs.table)

hs.insert(1)#
hs.insert(2)#
hs.insert(3)#
hs.insert(4)#
hs.insert(50)#
hs.insert(51)#
hs.insert(45)#
hs.insert(578)#
hs.insert(54)#
hs.insert(54)#
hs.insert(52)#
hs.insert(51)#
hs.insert(987)#
hs.insert(34)#
hs.insert(556)#
hs.insert(24)#

# print(hs.search(5))

# for item in hs.table:
#     print(item)
# print(hs.table[2])

# # print(hs.table[4])
# print(hs.items_count)
# print(hs.table_size)

# print(hs.search(1))
# print(hs.search(2))
# print(hs.search(3))
# print(hs.search(4))
# print(hs.search(50))
# print(hs.search(51))
# print(hs.search(45))
# print(hs.search(578))
# print(hs.search(54))
# print(hs.search(54))
# print(hs.search(52))
# print(hs.search(51))
# print(hs.search(987))
# print(hs.search(34))
# print(hs.search(556))
# print(hs.search(24))

hs.remove(1000)
print(hs.search(578))
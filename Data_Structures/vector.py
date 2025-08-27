class Vector:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.arr = [0] * self.capacity
        
    def push_back(self, val):
        if self.size == self.capacity:
            self.capacity *= 2
            
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
            
        new_arr[self.size] = val    
        self.arr = new_arr
        self.size += 1
        
    def insert(self, pos, value):
        if pos > self.size:
            raise ValueError("Vector Index Out Of Range")
        elif pos == self.size:
            self.push_back(value)
        elif self.size == self.capacity:
            self.capacity *= 2
            new_arr = [0] * self.capacity
            for i in range(self.size):
                new_arr[i] = self.arr[i]
               
            self.arr = new_arr
            
        for i in range(self.size, pos, -1):
            self.arr[i] = self.arr[i - 1]
        
        self.arr[pos] = value
              
        
    def __str__(self):
        return f"{self.arr[:self.size]}"
        
        
v = Vector()
print(v.arr)
v.push_back(1)
print(v.arr)
v.push_back(2)
print(v.arr)
v.push_back(3)
print(v.arr)
print(v.size)
print(v.capacity)
print(v)

v.insert(6, 25)
print(v)
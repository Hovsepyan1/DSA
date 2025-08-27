class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)
        
    def __get_right_child(self, index):
        return 2 * index + 1 
    
    def __get_left_child(self, index):
        return 2 * index + 2
    
    def __get_parent(self, index):
        return (index - 1) // 2
    
    def heapify(self, i, size):
        largestIndex = i
        l = self.__get_left_child(i)
        r = self.__get_right_child(i)
        if l < size and self.arr[l] > self.arr[largestIndex]:
            largestIndex = l
        if r < size and self.arr[r] > self.arr[largestIndex]:
            largestIndex = r
        if largestIndex == i:
            return 
        self.arr[i], self.arr[largestIndex] = self.arr[largestIndex], self.arr[i]
        self.heapify(largestIndex, size)
    
    def build_max_heap(self):
        for i in range(self.size // 2 - 1, -1, -1):
            self.heapify(i, self.size)
            
    def heap_sort(self):
        n = self.size 
        i = n - 1
        while i > 0:
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            n -= 1
            self.heapify(0, n)
            i -= 1
    
    def top(self):
        return self.arr[0]
    
    def pop(self):
        self.arr[0], self.arr[self.size - 1] = self.arr[self.size - 1], self.arr[0]
        self.arr.pop()
        self.size -= 1
        self.heapify(0, self.size)
    
    def push(self, value):
        self.arr.append(value)
        self.size += 1
        i = self.size - 1
        parent = self.__get_parent(i)
        while parent >= 0 and self.arr[parent] < self.arr[i]:
            self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
            i = parent
            parent = self.__get_parent(i)
            

    
# arr = [64, 30, 18, 94, 2, 3, 1, 15, 33, 55]
# ob = Heap(arr)
# ob.build_max_heap()
# print(ob.arr)
# # ob.pop()
# # ob.push(100)
# # print(ob.arr)
# # ob.heap_sort()
# # print(ob.arr)
# # ob.push(56)
# # print(ob.arr)

def heapify(arr, i, n):
    li = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[li]:
        li = l
    if r < n and arr[r] > arr[li]:
        li = r
    if i == li:
        return
    arr[i], arr[li] = arr[li], arr[i]
    heapify(arr, li, n)

def buildMaxHeap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)
    print(arr)


def heapSort(arr):
    buildMaxHeap(arr)
    n = len(arr)
    i = n - 1
    while i > 0:
        arr[0], arr[i] =  arr[i], arr[0]
        n -= 1
        heapify(arr, 0, n)
        i -= 1
        
arr = [64, 30, 18, 94, 2, 3, 1, 15, 33, 55]
heapSort(arr)
print(arr)


class Queue:
    def __init__(self):
        """Initialize the queue."""
        self.arr = []
    
    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.arr.append(item)
    
    def dequeue(self):
        """Remove and return the item from the front of the queue.
        
        Returns:
            The item from the front of the queue, or a message if the queue is empty.
        """
        if self.is_empty():
            print("Queue is empty")
            return
        item = self.arr.pop(0)
        return item
    
    def peek(self):
        """Return the item from the front of the queue without removing it.
        
        Returns:
            The item from the front of the queue, or a message if the queue is empty.
        """
        if self.is_empty():
            print("Queue is empty")
            return
        return self.arr[0]
    
    def is_empty(self):
        """Check if the queue is empty.
        
        Returns:
            True if the queue is empty, False otherwise.
        """
        return not bool(len(self.arr)) 
    
    def size(self):
        """Return the size of the queue.
        
        Returns:
            The number of items in the queue.
        """
        return len(self.arr)
    
    def clear(self):
        """Remove all items from the queue."""
        self.arr.clear()
    
    def display(self):
        """Display all the items in the queue.
        
        Returns:
            A list of all items in the queue.
        """
        print(self.arr)
        
        
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.display())  # Output: [10, 20, 30]
print(q.dequeue())  # Output: 10
print(q.peek())     # Output: 20
print(q.size())     # Output: 2
print(q.is_empty()) # Output: False
q.clear()
print(q.is_empty()) # Output: True

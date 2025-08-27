class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        return f"{self.val}"
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def insert(self, val):
        self.root = self.__insertHelper(self.root, val)
        self.size += 1
        
    def search(self, val):
        return self.__searchHelper(self.root, val)
        
    def remove(self, val):
        self.root = self.__removeHelper(self.root, val)

    def __insertHelper(self, node, val):
        if not node: return Node(val)
        if val < node.val:
            node.left = self.__insertHelper(node.left, val)
        else:
            node.right = self.__insertHelper(node.right, val)
            
        return node
        
    def __searchHelper(self, node, val):
        if not node: return False
        if val == node.val: return node
        if val < node.val:
            return self.__searchHelper(node.left, val)
        else:
            return self.__searchHelper(node.right, val)
    
    def __removeHelper(self, node, val):
        if not node:
            return None
        if val < node.val:
            node.left = self.__removeHelper(node.left, val)
        elif val > node.val:
            node.right = self.__removeHelper(node.right, val)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            succ = self.getMin(node.right)
            node.val = succ.val  # Replace value
            node.right = self.__removeHelper(node.right, succ.val)  # Delete successor

        return node
            
    def getHeight(self, node):
        if not node: return 0
        
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        return max(left, right) + 1
    
    def getMin(self, node):
        tmp = node
        while tmp.left:
            tmp = tmp.left
            
        return tmp
            
    def getMax(self, node):
        tmp = node
        while tmp.right:
            tmp = tmp.right
        
        return tmp

    def getSuccessor(self, val):
        succ = None
        tmp = self.root
        while tmp:
            if tmp.val <= val:
                tmp = tmp.right
            else:
                succ = tmp
                tmp = tmp.left
                
        return succ
    
    def getPredecessor(self, val):
        pred = None
        tmp = self.root
        while tmp:
            if tmp.val >= val:
                tmp = tmp.left
            else:
                pred = tmp
                tmp = tmp.right
                
        return pred
    

    def preorderTraversal(self, node):
        if not node: return
        
        print(node.val, end=" ")
        self.preorderTraversal(node.left)
        self.preorderTraversal(node.right)
        
    def inorderTraversal(self, node):
        if not node: return
        
        self.inorderTraversal(node.left)
        print(node.val, end=" ")
        self.inorderTraversal(node.right)


    def postorderTraversal(self, node):
        if not node: return
        
        self.postorderTraversal(node.left)
        self.postorderTraversal(node.right)
        print(node.val, end=" ")
        
        
        
# # Initialize the BST
# bst = BinarySearchTree()

# # Insert test cases
# nums = [50, 17, 72, 12, 23, 9, 14, 19, 67, 76, 54]
# for num in nums:
#     bst.insert(num)

# # Inorder Traversal (should print values in sorted order)
# print("Inorder Traversal:")
# bst.inorderTraversal(bst.root)  # Expected Output: 9 12 14 17 19 23 50 54 67 72 76
# print("\n")

# # Search test cases
# print("Search 19:", bst.search(19).val if bst.search(19) else "Not found")  # Expected: 19
# print("Search 100:", bst.search(100))  # Expected: Not found (False)

# # Min and Max test cases
# print("Min Value:", bst.getMin(bst.root).val)  # Expected: 9
# print("Max Value:", bst.getMax(bst.root).val)  # Expected: 76

# # Get Successor test cases
# succ = bst.getSuccessor(17)
# print("Successor of 17:", succ.val if succ else "None")  # Expected: 19

# succ = bst.getSuccessor(76)
# print("Successor of 76:", succ.val if succ else "None")  # Expected: None

# # Get Predecessor test cases
# pred = bst.getPredecessor(72)
# print("Predecessor of 72:", pred.val if pred else "None")  # Expected: 67

# pred = bst.getPredecessor(9)
# print("Predecessor of 9:", pred.val if pred else "None")  # Expected: None

# # Remove test cases
# print("\nBefore Removing 17:")
# bst.inorderTraversal(bst.root)
# print("\n")

# bst.remove(17)  # Remove 17 (it has children)

# print("After Removing 17:")
# bst.inorderTraversal(bst.root)  # Expected: 9 12 14 19 23 50 54 67 72 76
# print("\n")

# bst.remove(9)  # Remove leaf node
# print("After Removing 9:")
# bst.inorderTraversal(bst.root)  # Expected: 12 14 19 23 50 54 67 72 76
# print("\n")

# bst.remove(50)  # Remove root node
# print("After Removing 50 (Root Node):")
# bst.inorderTraversal(bst.root)  # Expected: 12 14 19 23 54 67 72 76
# print("\n")

# # Preorder Traversal
# print("Preorder Traversal:")
# bst.preorderTraversal(bst.root)  # Expected: 23 12 14 19 67 54 72 76
# print("\n")

# # Postorder Traversal
# print("Postorder Traversal:")
# bst.postorderTraversal(bst.root)  # Expected: 14 19 12 54 76 72 67 23
# print("\n")


# bst = BinarySearchTree()
# bst.insert(5)
# bst.insert(4)
# bst.insert(7)
# bst.insert(15)
# bst.insert(1)

# print(bst.getSuccessor(1).val)
# bst.inorderTraversal(bst.root)

# from collections import deque

# q = deque()  # Create a queue

# q.append(1)  # Enqueue
# q.append(2)
# q.append(3)

# a = q.popleft()
# b = q.
# print(a)
# print(q.popleft())  # Dequeue (FIFO)
# print(q.popleft())
# print(q.popleft())

# q.push(bst.root)
# while q.count():
#     size = q.count()
#     while size:
#         node = q.popleft()

# levels = {}
# ls = []
# ls.append(bst.root)

# while ls != []:
#     size = len(ls)
#     while size:
#         node = ls.pop(0)
#         print(node.val, end=" ")
#         if node.left:
#             ls.append(node.left)
#         if node.right:
#             ls.append(node.right)
#         size -= 1

# from collections import deque

# queue = deque()
# queue.append(bst.root)

# while queue:
#     size = len(queue)
#     while size:
#         node = queue.popleft()  # More efficient than pop(0)
#         print(node.val, end=" ")
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#         size -= 1

# class Solution:
#     def levelOrder(self, root):
#         bfs_ls = []
#         ls = []
#         ls.append(root)
#         while ls:
#             size = len(ls)
#             tmp_ls = []
#             while size:
#                 node = ls.pop(0)
#                 tmp_ls.append(node.val)
#                 if node.left:
#                     ls.append(node.left)
#                 if node.right:
#                     ls.append(node.right)   
#                 size -= 1
#             bfs_ls.append(tmp_ls)

#         return bfs_ls

b = BinarySearchTree()
b.insert(5)
b.insert(4)
b.insert(7)

# b.inorderTraversal(b.root)
print(b.getSuccessor(4))
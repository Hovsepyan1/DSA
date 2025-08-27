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
        
        bf = self.getBF(node)
        if bf > 1 and self.getBF(node.left) > 0:
            return self.rightRotate(node)
        elif bf > 1 and self.getBF(node.left) < 0:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        
        if bf < -1 and self.getBF(node.right) < 0:
            return self.leftRotate(node)
        elif bf < -1 and self.getBF(node.right) > 0:
            node.right = self.leftRotate(node.right)
            return self.leftRotate(node)
    
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
            
        bf = self.getBF(node)
        if bf > 1 and self.getBF(node.left) >= 0:
            return self.rightRotate(node)
        elif bf > 1 and self.getBF(node.left) < 0:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        
        if bf < -1 and self.getBF(node.right) <= 0:
            return self.leftRotate(node)
        elif bf < -1 and self.getBF(node.right) > 0:
            node.right = self.leftRotate(node.right)
            return self.leftRotate(node)

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
        
    def getBF(self, node):
        if not node:
            return 0
        return self.getHeight(node) - self.getHeight(node)
    
    def leftRotate(self, y):
        x = y.right
        t2 = x.left
        x.left = y
        y.right = t2
        return x
        
    def rightRotate(self, y):
        x = y.left
        t2 = x.right
        y.left = t2
        x.right = y
        
        return x
    
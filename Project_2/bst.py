class Node:
    def __init__(self, val):
        self.val = val        
        self.left = None      
        self.right = None     

def insert(root, val):
    if root is None:
        return Node(val)     
    
    if val < root.val:
        root.left = insert(root.left, val)   
    else:
        root.right = insert(root.right, val) 
    
    return root

def height(root):
    if root is None:
        return -1       
         
    return 1 + max(height(root.left), height(root.right))  

def maximum(root, l):
    if root is None:
        return None
    
    l.append(root.val)
    
    if root.right is None:
        return root.val
    
    return maximum(root.right, l)


def minimum(root, l):
    if root is None:
        return None
    
    l.append(root.val)

    if root.left is None:
        return root.val
    
    return minimum(root.left, l)

def bst_create(n):
    root = None
    
    for val in n:
        root = insert(root, val)   
    
    h = height(root)
    print("Wysokość drzewa BST:", h)

    l_max = []
    max_val = maximum(root, l_max)
    print(l_max, max_val)

    l_min = []
    min_val = minimum(root, l_min)
    print(l_min, min_val)


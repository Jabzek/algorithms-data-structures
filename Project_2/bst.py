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

def bst_create(n):
    root = None
    
    for val in n:
        root = insert(root, val)   
    
    h = height(root)
    print("Wysokość drzewa BST:", h)

n = list(map(int, input().split()))
bst_create(n)
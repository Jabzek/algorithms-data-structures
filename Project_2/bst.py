from node import Node

def insert(root, val):
    if root is None:
        return Node(val)     
    
    if val < root.val:
        root.left = insert(root.left, val)   
    else:
        root.right = insert(root.right, val) 
    
    return root

def bst_create(n):
    root = None
    
    for val in n:
        root = insert(root, val)   
    
    return root 

    


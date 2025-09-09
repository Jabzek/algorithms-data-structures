from node import Node
import math


def minimum_val(root):
    if root is None:
        return None

    if root.left is None:
        return root.val
    
    return minimum_val(root.left)

def delete_node(root, val, is_avl):
    if not root:
        return root
    
    if val < root.val:
        root.left = delete_node(root.left, val, is_avl)
    elif val > root.val:
        root.right = delete_node(root.right, val, is_avl)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        min_larger_node = minimum_val(root.right)
        root.val = min_larger_node
        root.right = delete_node(root.right, min_larger_node, is_avl)

    if is_avl:
        root = dsw_balance(root)

    return root

def in_order(root):
    if root:
        in_order(root.left)
        print(root.val, end=' ')
        in_order(root.right)

def pre_order(root):
    if root:
        print(root.val, end=' ')
        pre_order(root.left)
        pre_order(root.right)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val, end=' ')


def delete_whole_tree_post_order(root):
    if root:
        delete_whole_tree_post_order(root.left)
        delete_whole_tree_post_order(root.right)
        print("Usuwam węzeł:", root.val)
        root.left = None
        root.right = None
    return None

def tree_to_vine(root):
    tail = dummy = Node(None)
    dummy.right = root
    rest = root
    
    while rest:
        if rest.left:
            temp = rest.left
            rest.left = temp.right
            temp.right = rest
            rest = temp
            tail.right = temp
        else:
            tail = rest
            rest = rest.right
    return dummy.right

def compress(root, count):
    scanner = dummy = Node(None)
    dummy.right = root
    
    for _ in range(count):
        child = scanner.right
        if child and child.right:
            grandchild = child.right
            child.right = grandchild.left
            grandchild.left = child
            scanner.right = grandchild
            scanner = grandchild
        else:
            break
    return dummy.right

def dsw_balance(root):
    vine_root = tree_to_vine(root)
    size = 0
    temp = vine_root
    
    while temp:
        size += 1
        temp = temp.right
    m = 2 ** int(math.log2(size + 1)) - 1
    balanced_root = compress(vine_root, size - m)
    
    while m > 1:
        m //= 2
        balanced_root = compress(balanced_root, m)
    return balanced_root

def height(root):
    if root is None:
        return -1       
         
    return 1 + max(height(root.left), height(root.right))  


def maximum(root, l):
    if root is None:
        return None
    
    l.append(root.val)
    
    if root.right is None:
        return root.val, l
    
    return maximum(root.right, l)


def minimum(root, l):
    if root is None:
        return None
    
    l.append(root.val)

    if root.left is None:
        return root.val, l
    
    return minimum(root.left, l)
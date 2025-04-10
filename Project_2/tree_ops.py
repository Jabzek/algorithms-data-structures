from node import Node
import math

def get_height(node):
    return node.height if node else 0

def update_height(node):
    if node:
        node.height = 1 + max(get_height(node.left), get_height(node.right))

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    update_height(y)
    update_height(x)
    return x

def left_rotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    update_height(x)
    update_height(y)
    return y

def get_min_node(root):
    current = root
    while current.left:
        current = current.left
    return current

def delete_node(root, val, is_avl=False):
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
        min_larger_node = get_min_node(root.right)
        root.val = min_larger_node.val
        root.right = delete_node(root.right, min_larger_node.val, is_avl)

    if is_avl:
        update_height(root)
        balance = get_balance(root)

        if balance > 1 and get_balance(root.left) >= 0:
            return right_rotate(root)
        if balance > 1 and get_balance(root.left) < 0:
            root.left = left_rotate(root.left)
            return right_rotate(root)
        if balance < -1 and get_balance(root.right) <= 0:
            return left_rotate(root)
        if balance < -1 and get_balance(root.right) > 0:
            root.right = right_rotate(root.right)
            return left_rotate(root)

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

def find_min_max(root):
    min_node = root
    while min_node.left:
        min_node = min_node.left
    max_node = root
    while max_node.right:
        max_node = max_node.right
    print("Najmniejszy element w drzewie:", min_node.val)
    print("Największy element w drzewie:", max_node.val)

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
    root = tree_to_vine(root)
    size = 0
    temp = root
    while temp:
        size += 1
        temp = temp.right
    m = 2 ** int(math.log2(size + 1)) - 1
    root = compress(root, size - m)
    while m > 1:
        m //= 2
        root = compress(root, m)
    return root

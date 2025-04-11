from node import Node


def build_avl_tree(data):
    if not data:
        return None

    mid = len(data) // 2
    root = Node(data[mid])
    root.left = build_avl_tree(data[:mid])
    root.right = build_avl_tree(data[mid+1:])
    
    return root

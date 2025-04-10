from node import Node
from tree_ops import update_height

def build_avl_tree(data):
    """
    Tworzy zrównoważone drzewo AVL z posortowanej listy danych.
    Zwraca korzeń drzewa AVL.
    """
    if not data:
        return None

    mid = len(data) // 2
    root = Node(data[mid])
    root.left = build_avl_tree(data[:mid])
    root.right = build_avl_tree(data[mid+1:])
    
    update_height(root)  # AVL potrzebuje wysokości

    return root

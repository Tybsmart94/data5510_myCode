from print_tree import *

class Node:

    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

def insert(node, key):
    if node is None:
        return Node(key)
    
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    
    return node

def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key, end=" ")
		inorder(root.right)

def main():
    root = None
    root = insert(root, 3)
    root = insert(root, 1)
    root = insert(root, 4)
    root = insert(root, 1)
    root = insert(root, 5)
    root = insert(root, 9)

    print("Inorder traversal of the given tree")
    inorder(root)
    # PrintTree(root)

    print()
    display(root)

    root = insert(root, 3000)

    print("New")
    display(root)

main()


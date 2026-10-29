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

def find(node, key):
    if node is None:
        return False
    if node.key == key:
        # print("Reached an empty node")
        return True

    # print("Checking:", node.key)

    if key < node.key:
        return find(node.left, key)
    else:
        return find(node.right, key)
    
    return False

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

    print(find(root, 5))
    print(find(root, 3000))
    print(find(root, 22))

main()

"""
Chat prompts:
Why is the last line returning false? (Code included)

I changed it how you said to and it still returns false

Okay, I managed to fix it, can you explain to me in simple terms what was wrong and why those changes fixed it?

Alright, that makes sense, so I tested it with a value that isn't in my tree and it crashed. Shouldn't it just return false?
"""

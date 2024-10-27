class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        elif key > root.val:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "L --- ")
            print_tree(root.right, level + 1, "R --- ")

# Get user input for building the binary search tree
user_input = input("Enter space-separated values to build the Binary Search Tree: ")
values = list(map(int, user_input.split()))
while True:
    
# Construct the Binary Search Tree
bst_root = None
for value in values:
    bst_root = insert(bst_root, value)

# Get user input for search operation
search_key = int(input("Enter a value to search in the Binary Search Tree: "))

# Perform search operation
result = search(bst_root, search_key)

# Display the result
if result:
    print(f"Value {search_key} is found in the Binary Search Tree.")
else:
    print(f"Value {search_key} is not found in the Binary Search Tree.")

# Print the Binary Search Tree
print("\nBinary Search Tree:")
print_tree(bst_root)

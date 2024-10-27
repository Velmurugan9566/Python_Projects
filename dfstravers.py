class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def dfs_insert(root, key):
    if root is None:
        return Node(key)
    
    stack = [root]

    while stack:
        current_node = stack.pop(0)

        if not current_node.left:
            current_node.left = Node(key)
            break
        else:
            stack.append(current_node.left)

        if not current_node.right:
            current_node.right = Node(key)
            break
        else:
            stack.append(current_node.right)

    return root
def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "L --- ")
            print_tree(root.right, level + 1, "R --- ")
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)
   
def preorder_traversal(root):
    if root:
        print(root.val, end=' ')
        inorder_traversal(root.left)
        inorder_traversal(root.right)
    
def postorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        inorder_traversal(root.right)
        print(root.val, end=' ')


# Construct the binary tree using DFS insertion
tree_root = None
while True:
    print('\n1insert\n2.inorder\n3.preorder\n4.postorder\n5.exit')
    ch=int(input('enter choice: '))
    if ch==1:
        n=int(input('Enter the value to be insert:'))
        tree_root=dfs_insert(tree_root,n)
    elif ch==2:
        print('Inorder traversal;')
        inorder_traversal(tree_root)
        print()
    elif ch==3:
        print('preOrder traversal')
        preorder_traversal(tree_root)
        print()
    elif ch==4:
        print('postorder traversal')
        postorder_traversal(tree_root)
        print()
    elif ch==5:
        print_tree(tree_root)
       



class Node:
	def __init__(self, key):
		self.value = key
		self.left = None
		self.right = None

  #     1
  #   2   3
  # 4  5 6  7
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# traversal the tree

# Inorder Traversal: 
# 1. Traverse the left subtree, call Inorder(left subtree)
# 2. Visit the root
# 3. Traverse the right subtree, call Inorder(right subtree)

def inorder(root):
	if root is not None:
		inorder(root.left)
		print (root.value)
		inorder(root.right)
print("inorder")
inorder(root)

# Preorder Traversal
# 1. Visit the root
# 2. Traverse the left subtree, call Preorder(left substree)
# 3. Traverse the right subtree, call Preorder(right subtree)

def preorder(root):
	if root is not None:
		print(root.value)
		preorder(root.left)
		preorder(root.right)
print("preorder")
preorder(root)

# Postorder Traversal
# 1. Traverse the left subtree
# 2. Traverse the right subtree
# 3. Visit the root

def postorder(root):
	if root is not None:
		postorder(root.left)
		postorder(root.right)
		print(root.value)
print("postorder")
postorder(root)


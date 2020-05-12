
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def isValidBST(self, root: TreeNode) -> bool:
		if not root: return True
		stack = [(root, float("-inf"), float("inf"))]
		while stack:
			node, lower, upper = stack.pop()
			if node:
				val = node.val
				if node.val <= lower or node.val >= upper:
					return False
				stack.append((node.right, val, upper))
				stack.append((node.left, lower, val))
		return True


node = TreeNode(2)
left = TreeNode(1)
right = TreeNode(3)
node.left = left
node.right = right

node1 = TreeNode(1)
left1 = TreeNode(1)
node1.left = left1

node2 = TreeNode(10)
left2 = TreeNode(5)
right2 = TreeNode(15)
left3 = TreeNode(6)
right3 = TreeNode(20)
node2.left = left2
node2.right = right2
node2.right.left = left3
node2.right.right = right3

sol = Solution()
print(sol.isValidBST(node))
print(sol.isValidBST(node1))
print(sol.isValidBST(node2))



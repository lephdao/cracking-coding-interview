# Easy
# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode):
        if not root: return False
        queue = deque([root,root,])
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            if not node1 and not node2:
                if node1.val != node2.val: return False
                if not node1 or not node2: return False
                queue.append(node1.left)
                queue.append(node2.right)
                queue.append(node1.right)
                queue.append(node2.left)
        return True

# queue = [1,1], node1 = 1, node2 = 1
# queue = [2,2,2,2], node1 = 2, node2 = 2
# queue = [2,2,3,3,4,4], node1 = 2, node2 = 2
# queue = [3,3,4,4,3,3,4,4], node1 = 2, node2 = 2
#[1,2,2,3,4,4,3]
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(3)

test = Solution()
print({" Result ": test.isSymmetric(tree) })

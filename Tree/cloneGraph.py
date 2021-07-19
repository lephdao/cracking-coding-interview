import collections
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

"""Pseudocode:
"""
class Solution:
    # use BFS to traverse
    def cloneGraph(self, node: 'Node'):
        clone = {}
        # TODO: remove visited, clone can act as "visited"
        clone[node] = Node(node.val, [])
        queue = collections.deque([])
        queue.append(node)
        while queue:
            currentNode = queue.popleft()
            for neighbor in currentNode.neighbors:
                if (neighbor not in clone):
                    # we clone the node
                    clone[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                clone[currentNode].neighbors.append(clone[neighbor])

        return clone[node]

"""
Same concept as cloneGraph, except:
after 1st for loop we have: {1[2,4]:1, 2[1,3]:2, ...}
last for loop copies neighbors of key to neighbors of value
"""
def cloneGraphEasier(node: 'Node'):
    clone = {}
    clone[node] = Node(node.val, [])
    queue = collections.deque([])
    queue.append(node)
    while queue:
        currentNode = queue.popleft()
        for neighbor in currentNode.neighbors:
            if (neighbor not in clone):
                # we clone the node
                clone[neighbor] = Node(neighbor.val, [])
                queue.append(neighbor)
            #clone[currentNode].neighbors.append(clone[neighbor])
    for key in clone:
        for neighbor in key.neighbors:
            clone[key].neighbors.append(neighbor)

    return clone[node]

"""
1 - 2
|   |
4 - 3     equivalent to 1 [2,4], 2 [1,3], 3 [2,4], 4[1,3]
clone{1: 1[2,4], 2: 2[1,3], 4: 4[1,3], 3: 3[2,4]}
queue:
currentNode: 3
"""

solution = Solution()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node4, node2]
node4.neighbors = [node3, node1]
print(solution.cloneGraph(node1))

print(cloneGraphEasier(node1))

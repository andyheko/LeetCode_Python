"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        # a visited dictionary, key:old node, value: new node
        self.visited = {}
    def getCloneNode(self, node):
        if node:
            if node in self.visited: # if node already visited, return new node
                return self.visited[node]
            else: # if not, create a new node
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        old_node = head
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        while old_node != None: # iterate linked list unitl all nodes are cloned
            new_node.random = self.getCloneNode(old_node.random)
            new_node.next = self.getCloneNode(old_node.next)

            old_node = old_node.next
            new_node = new_node.next
        return self.visited[head]

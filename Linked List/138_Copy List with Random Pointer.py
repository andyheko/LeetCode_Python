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
        self.visited = {} # key: old node, value: new node
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        if head in self.visited: # if node already visited
            new_node = self.visited[head]
            return new_node
        else: # if not, create a new node
            new_node = Node(head.val, None, None)
            self.visited[head] = new_node

            new_node.next = self.copyRandomList(head.next)
            new_node.random = self.copyRandomList(head.random)
            return new_node

class Solution:
    def __init__(self):
        # a visited dictionary, key:old node, value: new node
        self.visited = {}
    def getCloneNode(self, node):
        if node:
            if node in self.visited: # if node already visited
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

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        curr = head
        while curr:
            new_curr = Node(curr.val, None, None)
            new_curr.next = curr.next
            curr.next = new_curr
            curr = new_curr.next

        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next

            old_list = head
            new_list = head.next
            new_head = head.next
        while old_list:
            old_list.next = old_list.next.next
            new_list.next = new_list.next.next if new_list.next else None

            old_list = old_list.next
            new_list = new_list.next
        return new_head

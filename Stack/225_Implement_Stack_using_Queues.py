class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.items.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.items.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.items[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if not self.items:
            return True
        else:
            False

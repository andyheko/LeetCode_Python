class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.items.append(x)


    def pop(self):
        """
        :rtype: None
        """
        self.items.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.items[-1]

    def getMin(self):
        """
        :rtype: int
        """
        minimum = float('inf')
        if not self.items:
            return None

        for i in self.items:
            if i < minimum:
                minimum = i
        return minimum

# Solution2:
#O(1)
# push a tuple with the first being the number pushed, the second being the minimum value so far
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        m = x
        if self.items:
            m = self.items[-1][1]
            if x < m:
                m = x
        self.items.append((x, m))

    def pop(self):
        """
        :rtype: void
        """
        self.items.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.items[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.items[-1][1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

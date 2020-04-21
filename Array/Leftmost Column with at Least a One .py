# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x, y):
#        """
#        :type x : int, y : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        row = binaryMatrix.dimensions()[0]
        col = binaryMatrix.dimensions()[1]
        r = row-1
        c = col-1
        while 0 <= r <= row-1 and 0 <= c <= col-1:
            if binaryMatrix.get(r, c) == 1: # if get 1 go left
                c -= 1
            elif binaryMatrix.get(r, c) == 0: # if get 0 go up
                r -= 1
        if c == col-1:
            return -1
        else:
            return c+1

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def backtrack(row, col, suffix):
            # base case: find match word
            if len(suffix) == 0:
                return True
            # check constraints
            if row < 0 or row == rows or col < 0 or col == cols or board[row][col] != suffix[0]:
                return False

            # mark the start to avoid visit agian before exploring
            board[row][col] = '#'
            for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                # explore neighbor directions
                if backtrack(row + rowOffset, col + colOffset, suffix[1:]):
                    return True
            # backtrack
            board[row][col] = suffix[0]
            # Tried all directions, not fina any match
            return False

        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, word):
                    return True
        return False

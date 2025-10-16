class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, word_i):
            if board[i][j] != word[word_i]:
                return False
            if word_i == len(word) - 1:
                return True
            char = board[i][j]
            board[i][j] = '*'
            coors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for r, c in coors:
                if 0 <= r < len(board) and 0 <= c < len(board[0]):
                    if dfs(r, c, word_i + 1):
                        return True
            board[i][j] = char
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False
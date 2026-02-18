class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        num = 0

        r, c = len(board), len(board[0])

        for i in range(r):
            for j in range(c):
                if board[i][j] == 'X':
                    num+=1
                    self.dfs(i, j, board, r, c)


        return num


    def dfs(self, i, j, board, r, c):
        if i < 0 or i >= r or j < 0 or j >= c or board[i][j]!='X':
            return

        board[i][j] = '.'
        self.dfs(i+1, j, board, r, c)
        self.dfs(i-1, j, board, r, c)
        self.dfs(i, j+1, board, r, c)
        self.dfs(i, j-1, board, r, c)


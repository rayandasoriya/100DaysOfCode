class Solution:
    def solve(self, board):
        """
            :type board: List[List[str]]
            :rtype: void Do not return anything, modify board in-place instead.
            """
        m = len(board)
        if m==0:
            return
        n = len(board[0])
        def helper(i,j):
            if i==-1 or i==m:
                return
            if j==-1 or j==n:
                return
            if board[i][j]=='O':
                board[i][j] = '1'
                helper(i+1,j)
                helper(i-1,j)
                helper(i,j+1)
                helper(i,j-1)
            return
        for i in range(m):
            helper(i,0)
            helper(i,n-1)
        for i in range(n):
            helper(0,i)
            helper(m-1,i)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='1':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'

class Solution(object):
    def exist(self, board, word):
        height = len(board)
        width = len(board[0])
        
        def go(i, j, depth):
            if depth >= len(word):
                return True
            
            if i < 0 or i >= height or j < 0 or j >= width:
                return False
            
            if board[i][j] == word[depth]:
                board[i][j] = '-'
                found =  go(i - 1, j, depth + 1) or \
                    go(i + 1, j, depth + 1) or \
                    go(i, j - 1, depth + 1) or \
                    go(i, j + 1, depth + 1)
                board[i][j] = word[depth]
                if found:
                    return True
            
            if depth == 0:
                return go(i, j + 1, depth) if j + 1 < width else go(i + 1, 0, depth)
                
        return False
        
    return go(0, 0, 0)

from collections import deque
class Solution(object):
    def numSquares(self, n):
        # edge case handling
        if n == 0:
            return 0
        
        # list of all possible squares to iterate over
        sqr_nums = [x*x for x in range(1, n+1)]
        
        d = deque()
        d.append(n)
        visited = set()
        levels = 0
        
        while d:
            levels += 1
            d_len = len(d)
            
            # this is to keep track of the current level in BFS
            for i in range(d_len):
                curr = d.popleft()
                for num in sqr_nums:
                    if curr - num  == 0:
                        return levels
                    elif curr - num < 0:
                        break
                    elif curr - num not in visited:
                        d.append(curr - num)
                        visited.add(curr - num)
    """
        :type n: int
        :rtype: int
        """

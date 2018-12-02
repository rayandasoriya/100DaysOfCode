class Solution:
    def findPaths(self, m, n, N, i, j):
        """
            :type m: int
            :type n: int
            :type N: int
            :type i: int
            :type j: int
            :rtype: int
            """
        
        num_path = 0
        step = N
        moves = [(1,0), (-1,0), (0,1), (0,-1)]
        to_visit = {(i, j):1}
        print to_visit
        while(step>0):
            new_to_visit = {}
            for k, v in to_visit.items():
                vx, vy = k
                v = v%(10**9+7)
                
                for mx, my in moves:
                    nx, ny = mx + vx, my + vy
                    if nx<0 or ny<0 or nx>=m or ny >=n:
                        num_path += v
                    elif (nx, ny) in new_to_visit:
                        new_to_visit[(nx, ny)] += v
                    else:
                        new_to_visit[(nx, ny)] = v
        to_visit = new_to_visit
            step -= 1
        return num_path%(10**9+7)

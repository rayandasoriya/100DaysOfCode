class Solution(object):
    def __init__(self):
        self.mem = { 0 : 0, 1 : 1, 2 : 2 }
    
    def climbStairs(self, n):
        
        if n in self.mem.keys():
            return self.mem[n]
        else:
            self.mem[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.mem[n]

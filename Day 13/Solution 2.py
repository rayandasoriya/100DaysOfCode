class Solution:
    
    def __init__(self, n_rows, n_cols):
        """
            :type n_rows: int
            :type n_cols: int
            """
        self.rows = [x for x in range(n_rows)]
        
        
        self.cols = [x for x in range(n_cols)]
        random.shuffle(self.rows)
        random.shuffle(self.cols)
        self.i = 0
    
    def flip(self):
        """
            :rtype: List[int]
            """
        
        value = [self.rows[self.i//len(self.cols)],self.cols[self.i%len(self.cols)]]
        self.i+=1
        return value
    
    
    def reset(self):
        """
            :rtype: void
            """
        self.i = 0
        if len(self.rows)>1:
            idx = random.randint(1,len(self.rows)-1)
            self.rows[0],self.rows[idx] = self.rows[idx],self.rows[0]
        if len(self.cols)>1:
            idx = random.randint(1,len(self.cols)-1)
            self.cols[0],self.cols[idx] = self.cols[idx],self.cols[0] 

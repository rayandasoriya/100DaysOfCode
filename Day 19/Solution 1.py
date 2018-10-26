class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        step = 1
        pos = 1
        lines = {}
        for c in s:
            if pos not in lines:
                lines[pos] = c
            else:
                lines[pos]+=c
            pos+=step
            if pos==1 or pos==numRows:
                step*=-1
        sol = ""
        for i in range(1, numRows+1):
            try:
                sol+=lines[i]
            except:
                return sol
        return sol

class Solution:
    def rotatedDigits(self, N):
        set1 = {'0', '1', '8', '2', '5', '6', '9'}
        set2 = {'2', '5', '6', '9'}
        res = 0
        for i in range(1, N+1):
            i_str = str(i)
            if self.all_in_set(set1, i_str) and self.any_in_set(set2, i_str):
                res +=1
        return res
    
    
    def all_in_set(self, s, string):
        for e in string:
            if e not in s:
                return False
        return True
    
    def any_in_set(self, s, string):
        for e in string:
            if e in s:
                return True
        return False

class Solution(object):
    def grayCode(self, n):
        ans = [0]
        
        for i in range(n):
            tmp = list(map(lambda x: x | 1 << i, ans))
            tmp.reverse()
            ans = ans + tmp
        
        return ans

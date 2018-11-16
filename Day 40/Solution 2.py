
class Solution:
    def integerBreak(self, C):
        """
            :type n: int
            :rtype: int
            """
        if C == 1:
            return 1
    
        vmax = 0
        for i in range(C, 1, -1):
            a, bt = divmod(C, i)
            b, at = (a + 1, i - bt)
            vmax = max(vmax, a ** at * b ** bt)

        return vmax

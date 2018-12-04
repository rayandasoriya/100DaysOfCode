class Solution:
    def largestPalindrome(self, n):
        # A joke version because n is [1,8]
        # 100% (32ms)
        # rst = [9, 987, 123, 597, 677, 1218, 877, 475]
        # return rst[n-1]
        
        # 75% (44ms)
        if n==1: return 9
        m = 10**n
        for a in range(2, 9*10**(n-1)):
            upper = m - a
            lower = int(str(upper)[::-1])
            # x*x - ax + lower = 0
            c = a**2 - 4*lower
            if c < 0: continue
            if c**.5 == int(c**.5):
                return (m * upper + lower) % 1337

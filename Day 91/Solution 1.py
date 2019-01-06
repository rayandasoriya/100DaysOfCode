class Solution(object):
    def countPrimes(self, n):
        """
            :type n: int
            :rtype: int
            """
        if n <= 1:
            return 0
        
        nums = [None] * n
        nums[0] = False
        nums[1] = False
        
        for i in xrange(n):
            if nums[i] == None:
                nums[i] = True
                for j in xrange(i+i, n, i):
                    nums[j] = False
    
        return sum(nums)

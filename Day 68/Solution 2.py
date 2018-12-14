class Solution(object):
    def checkPerfectNumber(self, num):
        primes= [2,3,5,7,13,17,19,31]
        
        for prime in primes:
            if self.pn(prime) == num:
                return True
        
        return False
    
    
    def pn(self, p):
        return (1 << (p - 1)) * ((1 << p) - 1)

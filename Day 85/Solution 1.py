class Solution(object):
    def fairCandySwap(self, A, B):
        sum_a,sum_b = sum(A),sum(B)
        B = set(B)
        for x in A:
            if x+ (sum_b-sum_a)/2 in B:
                return [x,x+ (sum_b-sum_a)/2]
        """
            :type A: List[int]
            :type B: List[int]
            :rtype: List[int]
            """

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        tot=(C-A)*(D-B)+(G-E)*(H-F)
        if E<=C and F<=D and G>=A and H>=B:
            overlap=min((C-E),(G-A),(C-A),(G-E))*min((D-B),(H-F),(H-B),(D-F))
            return tot-overlap
        else:
            return tot
        """
            :type A: int
            :type B: int
            :type C: int
            :type D: int
            :type E: int
            :type F: int
            :type G: int
            :type H: int
            :rtype: int
            """

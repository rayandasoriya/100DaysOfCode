class Solution:
    # @param n, an integer
    def reverseBits(self, n):
        new_int = 0
        for i in range(32):
            if (n & 1 << i) > 0:
                new_int ^= 1 << (31 - i)
        return new_int

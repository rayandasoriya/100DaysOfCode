class Solution:
    def selfDividingNumbers(self, left, right):
        def self_dividing(n):
            x = n
            while x > 0:
                x, d = divmod(x, 10)
                if d == 0 or n % d > 0:
                    return False
            return True
        ans = []
        for n in range(left, right + 1):
            if self_dividing(n):
                ans.append(n)
        return ans
        """
            :type left: int
            :type right: int
            :rtype: List[int]
            """

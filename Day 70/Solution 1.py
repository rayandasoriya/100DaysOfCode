class Solution(object):
    def plusOne(self, digits):
        num = int(''.join(map(str, digits))) + 1
        return list(map(int,str(num)))
        """
            :type digits: List[int]
            :rtype: List[int]
            """

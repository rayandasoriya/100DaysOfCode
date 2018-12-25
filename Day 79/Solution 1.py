class Solution(object):
    def convertToBase7(self, num):
        """
            :type num: int
            :rtype: str
            """
        isNegative = False if num > 0 else True
        lst = []
        res = 0
        num = abs(num)
        while num > 0:
            lst.append(num%7)
            num = num/7
        for i in range(len(lst)):
            res += 10**i * lst[i]
        return str(-res if isNegative == True else res)

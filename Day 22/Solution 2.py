class Solution(object):
    def maxProfit(self, prices):
        even, odd, oldEven = 0, float('-inf'), 0
        for price in prices:
            even, odd, oldEven = max(even, odd + price), max(odd, oldEven - price), even
        return even

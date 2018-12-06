from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        return Counter(nums).most_common()[-1][0]

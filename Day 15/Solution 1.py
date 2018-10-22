from itertools import combinations

class Solution(object):
    def fourSum(self, nums, target):
        arr = []
        nums.sort()
        perm = combinations(nums, 4)
        for i in list(perm):
            if sum(i)== target and i not in arr:
                arr.append(i);
        return arr
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[List[int]]
            """

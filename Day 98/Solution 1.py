class Solution(object):
    def findDisappearedNumbers(self, nums):
        for i in xrange(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
    
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

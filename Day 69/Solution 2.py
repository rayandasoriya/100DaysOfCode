class Solution(object):
    def permuteUnique(self, nums):
        if len(nums)<=1:
            return [nums]
        res= []
        # prev = 0
        for i in range(len(nums)):
            if nums[i] not in nums[:i]:
                prev = i
                new_nums = nums[:i]+nums[i+1:]
                for k in self.permuteUnique(new_nums):
                    res.append([nums[i]] + k)
        return res
        """
            :type nums: List[int]
            :rtype: List[List[int]]
            """

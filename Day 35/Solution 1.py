class Solution(object):
    def threeSum(self, nums):
        """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
        list_ = []
        nums = sorted(nums)
        if len(nums)<3 or nums[0]>0:
            return list_
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[j]+nums[k] == -nums[i]:
                    list_.append([nums[i],nums[j],nums[k]])
                    while j < k-1 and nums[k-1]==nums[k]:
                        k -=1
                    while j+1 < k and nums[j+1]==nums[j]:
                        j +=1
                    j +=1
                    k -=1
                elif nums[j]+nums[k] > -nums[i]:
                    k -=1
                else:
                    j +=1
        return list_        

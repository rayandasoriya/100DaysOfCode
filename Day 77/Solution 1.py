class Solution(object):
    def findDuplicate(self, nums):
        l= sorted(nums)
        for i,v in enumerate(l):
            if(l[i]==l[i+1]):
                return v
        return -1

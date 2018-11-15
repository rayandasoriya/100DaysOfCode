class Solution(object):
    def matrixReshape(self, nums, r, c):
        original_size = len(nums) * len(nums[0])
        
        if r * c > original_size:
            return nums
        else:
            temp = [[0 for i in xrange(c)] for j in xrange(r)]
            #Flatten the original num
            nums_flattened = [i for row in nums for i in row]
            for i in xrange(r):
                for j in xrange(c):
                    temp[i][j] = nums_flattened[i * c + j]
            
    nums = temp
        return nums
        """
            :type nums: List[List[int]]
            :type r: int
            :type c: int
            :rtype: List[List[int]]
            """

class Solution(object):
    def sortArrayByParity(self, A):
        array = []
        for nums in A:
            if nums%2 == 0:
                array.append(nums)
        for nums in A:
            if nums%2 == 1:
                array.append(nums)
        return array
        """
            :type A: List[int]
            :rtype: List[int]
            """

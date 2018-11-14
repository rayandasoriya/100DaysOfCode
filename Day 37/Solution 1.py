class Solution(object):
    def lengthOfLIS(self, nums):
        """
            :type nums: List[int]
            :rtype: int
            """
        from bisect import bisect
        subseq = []
        for num in nums:
            if not subseq or num > subseq[-1]:
                subseq.append(num)
            elif num < subseq[-1]:
                idx = bisect(subseq,num)
                if num != subseq[idx-1]: # deal with duplicate
                    subseq[idx]=num
        return len(subseq)


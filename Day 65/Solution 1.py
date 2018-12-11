class Solution(object):
    def diStringMatch(self, S):
        low, high = 0, len(S)
        ans = []
        for x in S:
            if x =='I':
                ans.append(low)
                low+=1
            if x == 'D':
                ans.append(high)
                high-=1
        return ans+[low]
        """
            :type S: str
            :rtype: List[int]
            """

from itertools import permutations
class Solution(object):
    def largestTimeFromDigits(self, A):
        hour = 0
        minu  = 0
        fin = -1
        a = permutations(A)
        for m,n,o,p in a:
            hours = 10*m+n
            mins = 10*o+p
            t_time = 60 * hours + mins
            if hours < 24 and mins < 60 and t_time > fin and hours>=0 and mins>=0:
                fin = t_time
                hour = hours
                minu = mins
        
        hour = str(hour) if len(str(hour))>1 else '0'+str(hour)
        minu = str(minu) if len(str(minu))>1 else '0'+str(minu)
        return str(hour)+':'+str(minu) if fin>=0 else ""
        
        
        
        """
            :type A: List[int]
            :rtype: str
            """

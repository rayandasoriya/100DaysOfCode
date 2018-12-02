class Solution(object):
    def isNStraightHand(self, hand, W):
        """
            :type hand: List[int]
            :type W: int
            :rtype: bool
            """
        N = len(hand)
        if N % W:
            return False
        count = collections.Counter(hand)
        for n in sorted(count):
            if not count[n]:
                continue
            for i in range(n+1, n+W):
                if count[i] < count[n]:
                    return False
                count[i] -= count[n]
return True

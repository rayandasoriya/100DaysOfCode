class Solution:
    def thirdMax(self, nums):
        """
            :type nums: List[int]
            :rtype: int
            """
        heap = [-n for n in set(nums)]
        heapq.heapify(heap)
        res = []
        count = 0
        print(heap)
        while heap and count < 3:
            res.append(-heapq.heappop(heap))
            count += 1
        return res[2] if len(res) == 3 else res[0]

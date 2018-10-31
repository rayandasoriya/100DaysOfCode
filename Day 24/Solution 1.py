class Solution(object):
    def maxArea(self, height):
        water = 0
        head = 0
        tail = len(height) - 1
        
        for cnt in range(len(height)):
            
            width = abs(head - tail)
            
            if height[head] < height[tail]:
                res = width * height[head]
                head += 1
            else:
                res = width * height[tail]
                tail -= 1
            
            if res > water:
                water = res
    
    return water
        """
            :type height: List[int]
            :rtype: int
            """

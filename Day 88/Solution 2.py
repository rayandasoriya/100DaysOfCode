class Solution(object):
    def constructRectangle(self, area):
        stack = []
        k = int(area**0.5)
        
        while not stack:
            if area%k == 0:
                stack.append(k)
            k -= 1
        
        return [area/stack[0],stack[0]]    

from collections import defaultdict as dd
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        queue = []
        order = []
        ins = [0 for _ in range(numCourses)]
        outs = dd(list)
        for [tail, head] in prerequisites:
            ins[tail]+=1
            outs[head].append(tail)
        for i in range(numCourses):
            if ins[i]==0:
                queue.append(i)
                order.append(i)
        count = len(queue)
        while queue:
            n = queue.pop(0)
            for p in outs[n]:
                ins[p]-=1
                if ins[p]==0:
                    queue.append(p)
                    order.append(p)
                    count+=1
        return order if numCourses==count else []

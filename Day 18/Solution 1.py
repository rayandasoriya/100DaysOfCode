class Solution(object):
    def exclusiveTime(self, n, logs):
        stack = []
        times = [0] * n
        for log in logs:
            split = log.split(':')
            id, event, t = int(split[0]), split[1], int(split[2])
            if event == 'start':
                stack.append([id, t, 0])
            else:
                sId, sStart, sOffset = stack.pop()
                dt = t - sStart + 1 - sOffset
                times[sId] += dt
                if stack:
                    stack[-1][2] += (dt + sOffset)
        return times

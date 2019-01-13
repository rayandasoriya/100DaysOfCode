class Solution(object):
    def numberOfBoomerangs(self, points):
        res = 0
        for p0 in points:
            distmap = collections.defaultdict(int)
            for p1 in points:
                dist = (p0[0]-p1[0]) ** 2 + (p0[1]-p1[1]) ** 2
                distmap[dist] += 1
            for p in distmap:
                res += distmap[p] * (distmap[p]-1)

    return res

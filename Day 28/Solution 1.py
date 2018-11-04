class Solution:
    def fourSum(self, a, t):
        a = sorted(a)
        n = len(a)
        ans = set()
        for i in range(n-3):
            for j in range(i+1, n-2):
                rem = t - a[i] - a[j]
                l, r = j+1, n-1
                while l < r:
                    if a[l] + a[r] == rem:
                        ans.add(tuple([a[i], a[j], a[l], a[r]]))
                        l += 1
                    elif a[l] + a[r] < rem: l+= 1
                    else: r -= 1
        return sorted([list(x) for x in ans])

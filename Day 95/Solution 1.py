class Solution:
    def findLongestWord(self, s, d):
        def helper(s, s2):
            if len(s2) > len(s):
                return False
            i = 0
            j = 0
            while i < len(s) and j < len(s2):
                if s[i] == s2[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            return j == len(s2)
        
        maxstr = ""
        maxlen = 0
        for s2 in d:
            if len(s2) >= maxlen:
                if len(s2) == maxlen:
                    if s2 < maxstr and helper(s, s2):
                        maxstr = s2
                else:
                    if helper(s, s2):
                        maxstr = s2
                        maxlen = len(maxstr)
    return maxstr

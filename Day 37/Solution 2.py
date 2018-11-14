class Solution:
    def repeatedSubstringPattern(self, s):
        length = len(s)
        if length <= 1:
            return False
        for i in range(1, int(length/2) + 1):
            if length % i == 0:
                str = s[i:] + s[0:i]
                if str == s:
                    return True
        return False

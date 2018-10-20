class Solution:
    def myAtoi(self, s):
        s = s.strip()
        try:
            val = ''
            for i in range(len(s)):
                if (s[i] in '+-' and i == 0) or '0' <= s[i] <= '9':
                    val += s[i]
                else: break
            val = int(val)
            if val < -2**31: return -2**31
            if val > 2**31-1: return 2**31-1
            return val
        except:
            return 0
        """
            :type str: str
            :rtype: int
            """

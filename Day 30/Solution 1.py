class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len=1
        end=1
        for i in range(1,len(s)):
            if i-max_len-1>=0 and s[i-max_len-1:i+1]==s[i-max_len-1:i+1][::-1]:
                max_len+=2
                end=i+1
                continue
            if s[i-max_len:i+1]==s[i-max_len:i+1][::-1]:
                max_len+=1
                end=i+1
        return s[end-max_len:end]
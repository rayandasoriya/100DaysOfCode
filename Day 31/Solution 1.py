class Solution(object):
    def countAndSay(self, n):
        """
            :type n: int
            :rtype: str
            """
        if n == 1:
            return "1"
        pre_list = list(self.countAndSay(n-1))
        res = ''
        count = 0
        cur_item= pre_list[0]
        for i in range(len(pre_list)):
            if pre_list[i] == cur_item:
                count = count+1
            else:
                res = res + str(count) + str(cur_item)
                cur_item = pre_list[i]
                count = 1
            if i == len(pre_list) -1:
                res = res + str(count) + str(cur_item)
        return res

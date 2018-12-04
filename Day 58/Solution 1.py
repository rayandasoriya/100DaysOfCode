class Solution:
    def findComplement(self, num):
        a=[]
        for i in bin(num)[2:]:
            if i =='0':
                a.append('1')
            else:
                a.append('0')
        return int(''.join(a),2)

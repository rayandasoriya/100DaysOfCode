
class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        isMinus= ((dividend<0 and divisor >0) or (dividend>0 and divisor <0));
        ret=0;
        dividend,divisor=abs(dividend),abs(divisor);
        c,sub=1,divisor;
        
        while(dividend >= divisor):
            if(dividend>=sub):
                dividend-=sub;
                ret+=c;
                sub=(sub<<1);
                c=(c<<1);
            else:
                sub=(sub>>1);
                c=(c>>1);
        
        if(isMinus):
            ret=-ret;
return min(max(-2147483648,ret),2147483647);

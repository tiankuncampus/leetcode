class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
 
        ret = 0
     
        x_abs = x if(x>=0) else -1*x
        
        while x_abs:
            ret = ret*10 + x_abs%10
            x_abs = x_abs//10
        
 
        ret = ret if(x>0) else ret*-1
    
        if ret < pow(-2,31) or ret > pow(2,31)-1:
            return 0
        
        return ret

s = Solution()
print(s.reverse(-10123))

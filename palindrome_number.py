class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x<0 or (x%10==0 and x!=0)):
            return False
        
        revert = 0
        while (revert < x):
            revert = revert*10 + x%10
            x //= 10
        
        return (x==revert or x==revert//10)
        
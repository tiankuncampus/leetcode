class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 0
        r_i = 0
        r_j = 0
        pal=dict()
        for i in range(0, len(s)):
            pal[i]=dict()
            for j in range(0,i+1):
                if (i==j):
                    pal[i][j] = True
                elif (i-j == 1):
                    pal[i][j]= s[i]==s[j]
                else:
                    pal[i][j] = True if(pal[i-1][j+1] and s[i]==s[j]) else False
                
                if (pal[i][j]):
                    if (i-j+1 > max_len):
                        max_len = i-j+1
                        r_i = i
                        r_j = j
        return s[r_j:r_i+1]

ss = Solution()
print(ss.longestPalindrome('abbcacbefea'))
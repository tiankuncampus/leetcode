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
                    if s[i]==s[j]:
                        pal[i][j]= True
                else:
                    if((j+1 in pal[i-1]) and s[i]==s[j]):
                        pal[i][j] = True 
                
                if (j in pal[i]):
                    if (i-j+1 > max_len):
                        max_len = i-j+1
                        r_i = i
                        r_j = j
        return s[r_j:r_i+1]

ss = Solution()
print(ss.longestPalindrome('abbcacbefea'))
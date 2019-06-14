'''
递归回朔解法
'''
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0

        if len(p) == 1:
            return len(s) == 1 and (s[0] == p[0] or p[0] == '.')
        
        if p[1] != '*': #模式第二个元素为不*
            if (len(s) > 0) and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        
        else: #第二个元素为*
            if self.isMatch(s, p[2:]):  #*前元素一次都不用
                 return True 
            i = 0
            while i < len(s) and (s[i] == p[0] or p[0] == '.'):
                if self.isMatch(s[i+1:], p[2:]):    #*前元素匹配i+1次
                    return True
                i+=1
        
        return False
'''

'''
动态规划解法
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False]*(len(p)+1) for i in range(len(s)+1)]
        dp[0][0] = True  #s前i 各元素  和p 前j个元素   是否模式匹配

        #空的s 和 模式p 的前j个元素的模式匹配的情况
        for j in range(2, len(p)+1):
            dp[0][j] = dp[0][j-2] and (p[j-1] == '*')

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1]=='.')
                else:
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (p[j-2]==s[i-1] or p[j-2]=='.'))
        
        return dp[-1][-1]


 



            




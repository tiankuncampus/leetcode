class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0 for i in range(m)] for j in range(n)]
        for i in range(0,m):
            res[0][i] = 1
        
        for i in range(0,n):
            res[i][0]=1
        
        for i in range(1,n):
            for j in range(1,m):
                res[i][j] = res[i-1][j] + res[i][j-1]
        
        return res[n-1][m-1]


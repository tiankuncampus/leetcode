class Solution:
    def generateMatrix(self, n: 'int') -> 'List[List[int]]':
        if (n==0):
            return list()
        begin = 1
        end = n*n
        x1,y1,x2,y2=0,0,n-1,n-1
        matrix = list()
        for x in range(0,n):
            temp=list()
            for y in range(0,n):
                temp.append(0)
            print(temp)
            matrix.append(temp)
        while (x1 <= x2 and y1 <= y2 and begin <= end):
            for y in range(y1,y2+1):
                matrix[x1][y] = begin
                begin += 1
            x1 += 1

            for x in range(x1, x2+1):
                matrix[x][y2] = begin
                begin+=1
            y2 -= 1

            if (x2 >= x1):
                for y in range(y2, y1-1, -1):
                    matrix[x2][y] = begin
                    begin += 1
                x2 -= 1
            
            if (y1 <= y2):
                for x in range(x2, x1-1, -1):
                    matrix[x][y1] = begin
                    begin += 1
                y1 += 1
        return matrix

            
s=Solution()
print(s.generateMatrix(3))
                


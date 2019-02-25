class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        if (len(matrix) < 1):
            return list()
        ret = list()
        x1,y1,x2,y2 = 0,0,len(matrix)-1,len(matrix[0])-1
        while(x1 <= x2 and y1 <= y2):
            #left->right
            for y in range(y1, y2+1):
                ret.append(matrix[x1][y])
            x1 += 1
            #up->down
            for x in range(x1, x2+1):
                ret.append(matrix[x][y2])
            y2 -= 1
            #right->left
            if (x1 <= x2):
                for y in range (y2,y1-1,-1):
                    ret.append(matrix[x2][y])
                x2 -= 1
            #down->up
            if (y1 <= y2):
                for x in range(x2, x1-1, -1):
                    ret.append(matrix[x][y1])
                y1 += 1
        return ret

s=Solution()
print(s.spiralOrder([[1,2,3],[4,5,6]]))
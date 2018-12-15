class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        s_len = len(s)
        ret_s = str()

        for row in range(0,numRows):
            cycle = 0
            while True:
                if row == 0 or row == numRows-1:
                    index = row + 2*(numRows-1)*cycle
                    cycle += 1
                    if (index < s_len):
                        ret_s += s[index]
                    else:
                        break
                else:
                    index1 = row + 2*(numRows-1)*cycle
                    index2 = index1 + 2*(numRows-row-1)
                    cycle += 1
                    if (index1 < s_len):
                        ret_s += s[index1]
                    else:
                        break
                    
                    if (index2 < s_len):
                        ret_s += s[index2]
                    else:
                        break
        
        return ret_s





        
        
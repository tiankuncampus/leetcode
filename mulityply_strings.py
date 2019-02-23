class Solution:
    def multiply(self, num1: 'str', num2: 'str') -> 'str':
        if(num1=='0' or num2=='0'):
            return '0'
        res = list()
        time = list()
        for i in range(-1, -1*(len(num1)+1), -1):
            multi = time + self.multiplyone(num2, num1[i])
            res = self.addstring(res, multi)
            time.append(0)
        

        r_str=''
        for r in res:
            r_str = str(r) + r_str
        
        return r_str


    
    def addstring(self, num1: 'list', num2: 'list') -> 'list':
        diff_len = len(num1) - len(num2)
        if (diff_len < 0):
            return self.addstring(num2, num1)

        for i in range(0, diff_len):
            num2.append(0)

        res = list()
        carry = 0
        for i in range(0, len(num1)):
            sum = num1[i] + num2[i] + carry
            res.append((sum)%10)
            carry = sum // 10
        if carry != 0:
            res.append(carry)
        
        return res

        
    def multiplyone(self, num1, num2):
        multi_num = int(num2)
        carry = 0
        res = list()
        for i in (range(-1,-1*(len(num1)+1),-1)):
            multi_x = int(num1[i])
            multi = multi_x * multi_num + carry
            res.append(multi%10)
            carry = multi//10
        
        if (carry!=0):
            res.append(carry)
        
        return res


s = Solution()
print(s.multiply('301','102'))
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0

        if len(p) == 1:
            return len(s) == 1 and (s[0] == p[0] or p[0] == '.')
        
        if p[1] != '*':
            if (len(s) > 0) and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        
        else:
            if self.isMatch(s, p[2:]):
                 return True 
            i = 0
            while i < len(s) and (s[i] == p[0] or p[0] == '.'):
                if self.isMatch(s[i+1:], p[2:]):
                    return True
                i+=1
        
        return False






            




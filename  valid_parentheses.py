class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        symbolmap = {'{':'}','[':']','(':')'}
        
        symbols = list()
        for symbol in s:
            if (symbol=='[' or symbol=='(' or symbol == '{'):
                symbols.append(symbol)
            elif (not symbol or symbolmap.get(symbols[-1]) != symbol):
                return False
            else:
                symbols.pop()
        return not symbols


s = Solution()
print(s.isValid('[]'))

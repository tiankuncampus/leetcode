class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        list_len = len(nums)
        if (list_len == 0):
            return [[]]
        res = [[[] for i in range(list_len+1)] for j in range(list_len+1)]
        for i in range(list_len+1):
            res[0][i]=[[]]
        for i in range(1,list_len+1):
            for j in range(i,list_len+1):
                item = list()
                up = res[i-1][j-1]
                for it in up:
                    item.append(it + [nums[j-1]])
                left = res[i][j-1]
                for it in left:
                    item.append(it)
                res[i][j] = item
        ret = list()
        for i in range(list_len+1):
            ret += res[i][list_len]
        
        return ret



s=Solution()
print(s.subsets([1,2,3]))
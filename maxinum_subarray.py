
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        summ = 0
        max_sum = None
        for num in nums:
            if (summ > 0):
                summ += num
            else:
                summ = num
            if(max_sum==None or max_sum < summ):
                max_sum = summ
        return max_sum

            


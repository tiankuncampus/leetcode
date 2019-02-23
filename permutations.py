class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        res = list()
        if (len(nums) <= 1):
            res.append(nums)
            return res
        
        for i in range(0,len(nums)):
            nums[0],nums[i] = nums[i], nums[0]
            res_temp = self.permute(nums[1:])
            for list_item in res_temp:
                list_item.insert(0, nums[0])
                res.append(list_item)
        return res
    

    def swap(self, a, b):
        a,b = b,a
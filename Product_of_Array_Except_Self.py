class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        res = [1]
        num_len = len(nums)

        #compute left multi of each element
        for i in range(0, num_len-1):
            res.append(res[i]*nums[i])
        
        #res[i] = left*right
        right = 1
        for i in range(num_len-1, -1, -1):
            res[i] = res[i]*right
            right *= nums[i]
        
        return res


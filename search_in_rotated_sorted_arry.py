class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        if len(nums)==0:
            return -1
        position = self.find_rotate_pos(nums)

        result = self.binary_search(nums[0:position], target)
        if (result != -1):
            return result
        
        result = self.binary_search(nums[position:], target)
        if (result != -1):
            return position+result
        
        return -1

    def binary_search(self, nums, target):
        if len(nums)==0:
            return -1
        start = 0
        end = len(nums) - 1
        while (start < end):
            m = (start + end)//2
            if(nums[m] > target):
                end -= 1
            elif (nums[m] < target):
                start += 1
            else:
                return m
        if (nums[start] == target):
            return start
        else:
            return -1


    
    def find_rotate_pos(self, nums):
        start = 0
        end = len(nums) - 1 
        
        first = nums[0]
        while(start < end):
            candidate = (start + end)//2
            temp = nums[candidate]
            if (temp < first):
                end -= 1
            else:
                start += 1
        return start


s=Solution()
print(s.search([1,1,1,1],2))
class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
       
        num_len = len(nums)
        if (num_len == 1):
            return nums[0]
        
        m = nums[0]
        begin = 0
        end = len(nums)-1

        while(begin < end):
            while(begin < end):
                if (nums[end] < m):
                    nums[begin] = nums[end]
                    begin += 1
                    break
                else:
                    end -= 1
            while(begin < end):
                if (nums[begin] > m):
                    nums[end] = nums[begin]
                    end -= 1
                    break
                else:
                    begin += 1
        nums[end] = m
        if (num_len - end == k):
            return nums[end]
        elif (num_len - end > k):
            return self.findKthLargest(nums[end+1:num_len], k)
        else:
            return self.findKthLargest(nums[0:end], k-(num_len-end))


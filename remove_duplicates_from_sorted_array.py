class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        last = None
        index = 0
        for i in range(len(nums)):
            if (last == None or last != nums[index]):
                last = nums[index]
                index += 1
            else:
                nums.pop(index)
        return len(nums)
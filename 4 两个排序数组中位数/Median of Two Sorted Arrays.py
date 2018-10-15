class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        k = len(nums1) + len(nums2)
        if k%2 == 0:
            return (self.findKth(nums1,nums2, k//2-1) + self.findKth(nums1, nums2, k//2))/2
        else:
            return self.findKth(nums1, nums2, k//2)
        
    def findKth(self,nums1, nums2,k):
        if (len(nums1) < len(nums2)):
            return self.findKth(nums2, nums1, k)
        if (len(nums2)==0):
            return nums1[k]
        if (len(nums1) + len(nums2) == k+1):
            return max(nums1[-1], nums2[-1])
        if (k==0):
            return min(nums1[0], nums2[0])
        
        mid1 = min(len(nums1)-1, k//2)
        mid2 = min(len(nums2)-1, k//2)
    
        if nums1[mid1] > nums2[mid2]:
            if mid1 + mid2 > k-1:
                return self.findKth(nums1[:mid1],nums2, k)
            else:
                return self.findKth(nums2[mid2+1:],nums1, k-mid2-1)
        else:
            if mid1 + mid2 > k-1:
                return self.findKth(nums1,nums2[:mid2], k)
            else:
                return self.findKth(nums1[mid1+1:], nums2, k-mid1-1)
            
           
            
s=Solution()
print(s.findMedianSortedArrays([1,2,3,4,11,14], [2,6,9,]))           
            
        
        
        
        
        
        
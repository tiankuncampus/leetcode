# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    a = 0
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root == None:
            return None
        ret = self.kthSmallest(root.left, k)
        if (self.a == k):
            return ret
        
        self.a += 1
        if (self.a == k):
            return root.val
        
        return self.kthSmallest(root.right, k)
        
        
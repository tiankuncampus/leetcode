# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    max_sum = -100000
    def maxPathSum(self, root: TreeNode) -> int:
        self.doMaxPathSum(root)
        return self.max_sum

    def doMaxPathSum(self, root: TreeNode) -> int:
        if root==None:
            return 0
        ret = root.val
        ret_left = self.doMaxPathSum(root.left)
        ret_right = self.doMaxPathSum(root.right)
        print("ret",ret, "left", ret_left, "right", ret_right)
        
        max_child = max(ret_left, ret_right)
        if (ret_left > 0):
            ret += ret_left
        if (ret_right > 0):
            ret += ret_right
        
        if (self.max_sum < ret):
            self.max_sum = ret
        return root.val + max_child if max_child>0 else root.val

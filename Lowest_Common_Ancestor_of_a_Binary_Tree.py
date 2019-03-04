#Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findPath(self, root, target, path):
        if root == None:
            return
        elif root == target:
            path.append(root)
            return path
        path.append(root)
        ret = self.findPath(root.left, target, path)
        if (ret):
            return ret
        ret = self.findPath(root.right, target, path)
        if (ret):
            return ret
        path.pop(-1)
        return None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = list()
        path2 = list()
        path1 = self.findPath(root, p, path1)
        path2 = self.findPath(root, q, path2)

        if (len(path1)==0 or len(path2)==0):
            return None
        
        i = 0
        while(i<len(path1) and i < len(path2)):
            if (path1[i] == path2[i]):
                i += 1
            else:
                break
        return path1[i-1]
            
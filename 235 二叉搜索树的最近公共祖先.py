### 解题思路
利用二叉搜索树的性质，当跟节点小于两个节点的值，递归右子树搜索
当跟节点大于两个节点的值，递归左子树搜索

### 代码

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val <p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif root.val >p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        return root

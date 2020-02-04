### 解题思路
递归

### 代码

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.res=0
        def dfs(root,pre):
            if root:
                if not root.left and not root.right:
                    self.res+=int(pre+str(root.val),2)
                    return
                dfs(root.left,pre+str(root.val))
                dfs(root.right,pre+str(root.val))
        dfs(root,'')
        return self.res

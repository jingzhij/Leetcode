#思路：用哈希表记录深度和列数，最后排序输出
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import defaultdict
        hashmap=defaultdict(list)
        def helper(root,col,depth):
            if not root:
                return None
            hashmap[col].append([depth,root.val])
            helper(root.left,col-1,depth+1)
            helper(root.right,col+1,depth+1)
        helper(root,0,0)
        res=[]
        return [[b for a,b in sorted(v,key=lambda x:x[0])] for k,v in sorted(hashmap.items())]





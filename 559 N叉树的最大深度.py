"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        res=0
        for child in root.children:
            res=max(self.maxDepth(child),res)
        return res+1
        
#迭代        
        # if not root:
        #     return 0
        # deque=collections.deque()
        # deque.append(root)
        # res=0
        # while deque:
        #     count=len(deque)
        #     res+=1
        #     for i in range(count):
        #         node=deque.popleft()
        #         for i in node.children:
        #             deque.append(i)
        # return res
        



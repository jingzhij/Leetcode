### 解题思路
此处撰写解题思路

### 代码

```
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def sym(root1,root2):
            if  root1==None and  root2==None:
                return True
            elif root1==None or root2==None:
                return False         
            else :return root1.val==root2.val and sym(root1.left,root2.right) and sym(root1.right,root2.left)
        return sym(root,root)
            
```


```
deque=collections.deque()
deque.append(root)
while deque:
    temp=[]
    count=len(deque)
    for _ in range(count):
        node=deque.popleft()
        if not node:
            temp.append(None)
            continue
        else:
            temp.append(node.val)
        deque.append(node.left)
        deque.append(node.right)
    if temp!=temp[::-1]:
        return False
return True
```



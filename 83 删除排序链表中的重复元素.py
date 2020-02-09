### 解题思路
逐个向后扫描，如果下一个节点的值和当前想等，跳过

### 代码

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res=head
        while head:
            if head.next and head.next.val==head.val:
                head.next=head.next.next
            else:
                head=head.next
        return res


            
        
    
```

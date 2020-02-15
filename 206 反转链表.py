### 解题思路
迭代很简单，递归有点绕，大家需要仔细想一想，简单的说返回的节点都是最后一个节点，层层递归上去，从尾部开始处理
head.next.next=head,head.next=None, 第一行head.next是它后边的节点，head.next.next=head意思是它后边的节点指向它本身
这里形成了一个环，所以head.next=None，把前边指向后边的关系取消
### 代码

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        def reverse(hd):
            if not hd or not hd.next:
                return hd
            cur=reverse(hd.next)
            hd.next.next=hd
            hd.next=None
            return cur
        return reverse(head)
    迭代
 
        # if not head:
        #     return head
        # pre=None
        # cur = head
        # while head:
        #     tmp=head.next
        #     head.next=pre
        #     pre=head
        #     head=tmp
        # return pre

```

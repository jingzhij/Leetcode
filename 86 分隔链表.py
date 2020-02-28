思路：逐个比较，两个哑节点，一个记录比x大的链表，另一个记录比x小的链表，需要注意的一点是，最后合并的时候，将第二个链表末尾置None，否则会出现循环
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dm1=p1=ListNode(-1)
        dm2=p2=ListNode(-1)
        while head:
            if head.val<x:
                p1.next=head
                p1=p1.next
            else:
                p2.next=head
                p2=p2.next
            head=head.next
        p1.next=dm2.next
        p2.next=None
        return dm1.next

      

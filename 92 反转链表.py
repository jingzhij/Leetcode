思路：先找到反转开始的地方，并且记录反转开始前的位置为con
而后反转链表，记录反转后的头部和尾部为prev，和tail，
然后接上即可 con.next=prev, tail.next=cur
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        cur=head
        prev=None
        while m>1:
            prev=cur
            cur=cur.next
            m,n=m-1,n-1
        tail,con=cur,prev
        tail, con = cur, prev
        while n:
            tmp=cur.next
            cur.next=prev
            prev=cur
            cur=tmp
            n-=1
        if con:
            con.next=prev
        else:
            head=prev
        tail.next=cur
        return head
      

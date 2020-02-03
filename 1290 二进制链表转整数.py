# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res=0 #初始化答案为0
        while head:
            res = res * 2 + head.val  #res*2 相当于整体右移一位，再加上本次的数值
            head = head.next
        return res
 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        temp = head
        l = 0
        while temp:
            l += 1
            temp = temp.next
        if l == n:
            return head.next
        tail = head
        for i in range(l-n-1):
            tail = tail.next
        tail.next = tail.next.next
        return head

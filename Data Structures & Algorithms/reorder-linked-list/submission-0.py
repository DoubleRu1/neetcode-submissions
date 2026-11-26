# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        length = 0
        while temp:
            temp = temp.next
            length += 1
        tail = head
        for i in range((length+1)//2 - 1):
            tail = tail.next
        head2 = tail.next 
        tail.next = None

        pre = None
        while head2:
            temp = head2.next
            head2.next = pre
            pre = head2
            head2 = temp
        ans = head
        while pre:
            temp = head.next
            head.next = pre
            temp_pre = pre.next
            pre.next = temp
            pre = temp_pre
            head = temp
        head = ans

        
        

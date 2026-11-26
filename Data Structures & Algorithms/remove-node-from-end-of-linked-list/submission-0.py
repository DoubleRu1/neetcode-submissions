# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #get the length of linklist
        temp = head
        length = 0
        while temp:
            temp = temp.next
            length += 1
        
        # find the previous node of n
        pre = ListNode()
        ans = pre
        pre.next = head
        target = head
        idx = 0
        while target and idx != length-n:
            pre = target
            target = target.next
            idx += 1
        #delete target
        if target:
            pre.next = target.next 
            target.next = None
        else:
            pre.next = None
        return ans.next



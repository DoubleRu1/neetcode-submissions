# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> ListNode:
        if not head or head.next == None:
            return head
        tail = None
        while head:
            temp = head.next
            head.next = tail
            tail = head
            head = temp
        return tail
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head and head.next != None:
            length = 0
            temp = head
            while temp:
                length += 1
                temp = temp.next
            tail = head
            print(length)
            for i in range((length-1)//2):
                tail = tail.next
            # print((length-1)//2,tail.val)
            temp = tail.next
            tail.next = None
            tail = temp
            # print(tail.val)
            tail = self.reverse(tail)
            dummy_head = ListNode()
            new_head = dummy_head
            new_head.next = head
            new_head = head
            while head and tail:
                temp = head.next
                new_head.next = head
                new_head = head
                head.next = None
                head = temp
                temp = tail.next
                new_head.next = tail
                new_head = tail
                tail.next = None
                tail = temp
            if head:
                new_head.next = head
            if tail:
                new_head.next = tail
            head = dummy_head.next
            

        
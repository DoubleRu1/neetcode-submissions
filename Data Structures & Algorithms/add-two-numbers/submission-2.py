# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # calculate
        ans = ListNode()
        def get_num(node: ListNode) -> int:
            num,idx= 0,0
            while node:
                num = num + node.val * 10 ** idx
                node = node.next
                idx += 1
            return num
        num1 = get_num(l1)
        num2 = get_num(l2)
        total = num1 + num2
        dummy_head = ListNode()
        head = dummy_head
        if total == 0:
            return ListNode(0)
        while total != 0:
            new_node = ListNode(total % 10)
            head.next = new_node
            head = new_node
            total = total // 10
        return dummy_head.next
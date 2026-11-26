# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            dummy_head = ListNode()
            dummy_head.next = head
            nh = None
            while head:
                next_node = head.next
                head.next = nh
                nh = head
                head = next_node
            return nh, dummy_head

        dummy_head = ListNode()
        dummy_head.next = ListNode()
        ans_head = dummy_head
        node = head
        #find kth node
        while node:
            # 当前段的头部
            cur_head = node
            cur = node
            i = 0
            # 最多循环k次
            while cur and i < k-1:
                i += 1
                cur = cur.next
            # 当长度达到要求
            if i == k-1 and cur:
                # 截断
                temp = cur.next
                cur.next = None
                cur = temp
                # reverse
                nh, dh = reverse(cur_head)
                print(nh.val,dh.val)
                # 前一段的尾部接到现在的头部
                if dummy_head:
                    dummy_head.next.next = nh
                dummy_head = dh
            else:
                if dummy_head:
                    dummy_head.next.next = cur_head
            node = cur
        
        return ans_head.next.next


        

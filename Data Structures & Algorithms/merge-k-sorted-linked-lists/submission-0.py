# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        dh = ListNode()
        head = dh
        counter = 0  # 唯一计数器，用于打破 val 相同时的比较
        for node in lists:
            heapq.heappush(heap,(node.val,counter,node))
            counter += 1
        
        while heap:
            _,_, t = heapq.heappop(heap)
            head.next = t
            head = head.next
            if t.next:
                heapq.heappush(heap,(t.next.val,counter,t.next))
                counter += 1
        
        return dh.next
            
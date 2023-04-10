# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        l, r = head, head.next
        p = head.next

        while l.next and r.next:
            l.next = l.next.next
            l = l.next
            r.next = r.next.next
            r = r.next

        l.next = p
        return head
        

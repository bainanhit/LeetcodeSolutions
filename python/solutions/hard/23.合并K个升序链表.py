# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 分治+归并 O(nklogk)
        n = len(lists)
        
        def mergeTwoLists(l1, l2):
            if not l1 or not l2:
                return l2 if not l1 else l1
            head = ListNode(0)
            p = head
            p1, p2 = l1, l2
            while l1 and l2:
                if l1.val < l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next
            p.next = l1 if l1 else l2
            return head.next
        
        def merge(l, r):
            if l == r:
                return lists[l]
            if l > r:
                return
            mid = (l + r) // 2
            l1 = merge(l, mid)
            l2 = merge(mid+1, r)
            
            return mergeTwoLists(l1, l2)
             
        return merge(0, n-1)
            






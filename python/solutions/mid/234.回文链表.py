# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 时间O(N) 空间O(1)
    def reverse(self, head):
        cur, pre = head, None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 快慢指针
        l, r = head, head
        while r and r.next:
            l = l.next
            r = r.next.next
        if r:
            l = l.next # 奇数个节点
        first = head
        last = self.reverse(l)
        
        while last:
            if first.val != last.val:
                return False
            first = first.next
            last = last.next
        
        return True
        
        
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        # 双指针
        dummy = ListNode(0, head)
        pre = dummy
        cur = pre.next
        while cur:
            next = cur.next
            while next and cur.val == next.val:
                next = next.next
            if next != cur.next:
                # next 移动过，说明中间存在重复元素，将 pre 的 next 指针指向
                pre.next = next
                cur = next
            else:
                # next 没有移动过
                pre = cur
                cur = cur.next

        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 快慢指针，先让快指针走k步，然后两个指针同步走，当快指针走到头时，慢指针就是链表倒数第k个节点
        if not head:
            return head
        fast, slow = head, head
        while(k):
            fast = fast.next
            k -= 1
        while(fast):
            fast = fast.next
            slow = slow.next
        return slow
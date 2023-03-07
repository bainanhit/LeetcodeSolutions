# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0 or not head.next:
            return head
        # 统计链表结点数
        cnt = 1
        cur = head
        # 从第2个节点开始遍历
        while cur.next:
            cur = cur.next
            cnt += 1
        
        k = k % cnt
        if k == 0:
            return head
        
        # 首尾相连
        cur.next = head
        # 移动后最后一个节点号
        for i in range(cnt-k):
             cur = cur.next
        
        head_new = cur.next
        cur.next = None

        return head_new
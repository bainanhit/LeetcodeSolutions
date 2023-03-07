# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        pre, end = dummy, dummy

        while end.next:
            # 取出待翻转的部分
            i = 0
            while i < k and end:
                end = end.next
                i += 1
            if not end: break

            # 断开链表
            startNode = pre.next
            nextNode = end.next
            end.next = None

            # 处理翻转 
            pre.next = self.reverse(startNode)
            # startNode 转到翻转这部分节点的最后了

            # 连接断开的链表
            startNode.next = nextNode

            # 挪动以进行下一组处理
            pre = startNode
            end = pre
        return dummy.next

    def reverse(self, head):
        pre = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = pre
            pre = curr
            curr = nextNode
        return pre
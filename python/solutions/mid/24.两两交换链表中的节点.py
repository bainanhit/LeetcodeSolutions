# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 递归
        # 不足两个节点，无需交换
        if not head or not head.next:
            return head

        node1 = head   
        node2 = head.next
        node3 = head.next.next

        node1.next = self.swapPairs(node3) # 1 指向递归返回的链表头
        node2.next = node1 # 2指向1
        
        return node2
        
        

            
            
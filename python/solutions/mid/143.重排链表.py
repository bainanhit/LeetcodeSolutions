# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.findMiddle(head)
        list1 = head
        list2 = mid.next
        list2 = self.reverseList(list2)
        mid.next = None
        self.mergeList(list1, list2)
        
    # find the middle point
    def findMiddle(self, head):
        if not head and not head.next:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    # reverse the second part of the list 
    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        
        return pre
    
    def mergeList(self, list1, list2):
        while list1 and list2:
            tmp1 = list1.next
            tmp2 = list2.next
            list1.next = list2
            list1 = tmp1
            list2.next = list1
            list2 = tmp2
            
            
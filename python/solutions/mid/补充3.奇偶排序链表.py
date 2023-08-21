# 题目： 给定一个奇数位升序，偶数位降序的链表，将其重新排序。
# 1. 按奇偶位置拆分链表，得1->3->5->7->NULL和8->6->4->2->NULL
# 2. 反转偶链表，得1->3->5->7->NULL和2->4->6->8->NULL
# 3. 合并两个有序链表，得1->2->3->4->5->6->7->8->NULL
class ListNode:    
    def __init__(self, x):        
        self.val = x        
        self.next = None

class Solution:    
    # O(N) Z(1)
    def sortOddEvenList(self,head):     
        if not head or not head.next:      
            return head        
        oddList,evenList = self.partition(head)        
        evenList = self.reverse(evenList)        
        return self.merge(oddList,evenList)    

    def partition(self, head: ListNode) -> ListNode:        
        evenHead = head.next        
        odd, even = head, evenHead        
        while even and even.next:            
            odd.next = even.next            
            odd = odd.next            
            even.next = odd.next            
            even = even.next        
        odd.next = None        
        return [head,evenHead]    
    def reverse(self,head):        
        dumpy = ListNode(-1)        
        p = head        
        while p:            
            temp = p.next            
            p.next = dumpy.next            
            dumpy.next = p            
            p = temp        
        return dumpy.next    
    def merge(self,p,q):        
        head = ListNode(-1)        
        r = head        
        while p and q:            
            if p.val <= q.val:               
                r.next = p                
                p = p.next            
            else:                
                r.next = q                
                q = q.next            
            r = r.next        
        if p:            
            r.next = p        
        if q:            
            r.next = q        
        return head.next
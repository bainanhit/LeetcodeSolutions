# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)
        
        
    def mergeSort(self, head):
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        next = slow.next
        slow.next = None
        left = self.mergeSort(head)
        right = self.mergeSort(next)
        
        return self.merge(left, right)
        
        
    
    def merge(self, left, right):
        dummy = ListNode(0)
        cur = dummy
        while left and right:
            if left.val > right.val:
                cur.next = right
                right = right.next
            else:
                cur.next = left
                left = left.next
            cur = cur.next
        
        if not left:
            cur.next = right
        else:
            cur.next = left
            
        return dummy.next
        
                
        
'''
//归并排序-递归
//时间复杂度O(nlogn)，空间复杂度O(logn)，其中n是链表的长度。空间复杂度主要取决于递归调用的栈空间。
//经典归并，许多题用到这个模板。 
class Solution {
    public ListNode sortList(ListNode head) {
        return mergeSort(head);
    }
    private ListNode mergeSort(ListNode head){
        if (head == null || head.next == null)//这个条件哪来的，我的想法是不能让fast.next为空
            return head;
        ListNode fast = head, slow = head;
        //偶数个节点找到中心左边的节点，好让slow.next=null，分成两段链表
       //记住这个判断条件，偶数结点会找靠左结点，奇数就是中间节点，能用到很多题上
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode next = slow.next;
        slow.next = null;
        ListNode left = mergeSort(head);
        ListNode right = mergeSort(next);
        return merge(left, right);
    }
    private ListNode merge(ListNode left, ListNode right){  //两个链表merge模板，用到的地方也很多
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        while(left != null && right != null){
            if(left.val > right.val){
                cur.next = right;
                right = right.next;
            }else{
                cur.next = left;
                left = left.next;
            }
            cur = cur.next;
        }
        cur.next = left != null ? left : right;
        return dummy.next;
    }
}
'''
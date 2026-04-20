# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        d=ListNode()
        d.next=head
        c=d
        while c and c.next:
            if c.next.val==val:
                c.next=c.next.next
            else:
                c=c.next
            
        return d.next
            
        
        
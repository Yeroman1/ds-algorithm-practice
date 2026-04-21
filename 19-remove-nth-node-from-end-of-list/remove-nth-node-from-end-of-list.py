# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=0
        temp=head
        while temp:
            c+=1
            temp=temp.next

        d=ListNode()
        d.next=head
        temp=d

        for i in range(c-n):
            temp=temp.next

        temp.next=temp.next.next
        return d.next

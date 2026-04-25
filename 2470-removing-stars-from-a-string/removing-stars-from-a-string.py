class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
class Solution:
    def removeStars(self, s: str) -> str:
        dummy=Node(0)

        for i in s:
            if i != "*":
                new_node=Node(i)
                new_node.next=dummy.next
                dummy.next=new_node
            else:
                dummy.next=dummy.next.next

        ans=''
        curr=dummy.next
        while curr:
            ans=curr.value+ans
            curr=curr.next
        
        return ans

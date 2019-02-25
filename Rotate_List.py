# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if (not head):
            return head
        temp = head
        len = 0
        while(temp):
            len += 1
            temp = temp.next
        
        k = k % len

        if k == 0:
            return head
        
        temp = ListNode
        temp.next = head
         
        r = temp
        for i in range(0,k):
            r = r.next
        l = temp
        while(r.next):
            l = l.next
            r = r.next
        r.next = head
        new_head = l.next
        l.next = None

        return new_head

        


        
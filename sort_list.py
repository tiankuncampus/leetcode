# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if (head == None or head.next == None):
            return head
        slow = head
        quick = head
        while(quick.next != None):
            quick = quick.next
            if (quick.next == None):
                break
            slow = slow.next
            quick = quick.next
        right = slow.next
        slow.next = None

        l_head = self.sortList(head)
        r_head = self.sortList(right)

        ret_head = ListNode(0)
        tail = ret_head
        while(r_head and l_head):
            if (l_head.val <= r_head.val):
                tail.next = l_head
                l_head = l_head.next
                tail = tail.next
            else:
                tail.next = r_head
                r_head = r_head.next
                tail = tail.next
        if (r_head):
            tail.next = r_head
        elif (l_head):
            tail.next = l_head
        else:
            tail.next = None
        
        return ret_head.next

                
        
        
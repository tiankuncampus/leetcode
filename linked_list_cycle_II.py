# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        help_head = ListNode(-1)
        help_head.next = head
        slow = help_head
        quick = help_head
        while(True):
            if(quick.next == None or quick.next.next == None):
                return None
            slow = slow.next
            quick = quick.next.next

            if (slow is quick):
                break
        
        slow_new = help_head
      
        while(not (slow_new is slow)):
            slow_new = slow_new.next
            slow = slow.next
        return slow
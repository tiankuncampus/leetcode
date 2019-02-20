# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        tail = head
        
        while (l1 or l2):
            if (l1 and l2):
                if (l1.val < l2.val):
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            elif (l1):
                tail.next = l1
            else:
                tail.next = l2
        
        return head.next
            




        
        
        
        
        
        
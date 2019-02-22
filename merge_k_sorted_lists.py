import heapq
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class UserNode:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(0)
        cur = head

        sortlist = list()
        for item in lists:
            if (item):
                heapq.heappush(sortlist, UserNode(item))
             
        while(len(sortlist) > 0):
            if (len(sortlist)==1):
                cur.next = sortlist[0].node
                break
            unode = heapq.heappop(sortlist)
            if (unode.node.next):
                heapq.heappush(sortlist, UserNode(unode.node.next))
            cur.next = unode.node
            cur = cur.next
        
        return head.next
            


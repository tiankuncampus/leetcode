class ListNode:
    def __init__(self, k: int, v: int):
        self.k = k
        self.v = v
        self.pre = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.kv = dict()
        self.head = ListNode(0, 0)
        self.tail = self.head
        self.size = 0
    
    def delNode(self, node: ListNode):
        node.pre.next = node.next
        if (node.next != None):
            node.next.pre = node.pre
        else:
            self.tail = node.pre
    
    def addHeadNode(self, node:ListNode):
        node.next = self.head.next
        node.pre = self.head
        if self.head.next != None:
            self.head.next.pre = node
        else:
            self.tail = node
        self.head.next = node
    
    def get(self, key: int) -> int:
        if key in self.kv:
            node = self.kv[key]
            self.delNode(node)
            self.addHeadNode(node)
            return node.v
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if -1 != self.get(key):
            self.kv[key].v = value
            return

        if self.size == self.capacity:
            self.kv.pop(self.tail.k)
            self.delNode(self.tail)
        else:
            self.size += 1
        
        
        node = ListNode(key, value)
        self.addHeadNode(node)
        self.kv[key] = node